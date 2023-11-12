import json
import sys
from pathlib import Path
from typing import List

from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import AzureOpenAIEmbeddings
from llama_index import (
    Document,
    LangchainEmbedding,
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from llama_index.indices.vector_store import GPTVectorStoreIndex
from llama_index.readers.file.markdown_reader import MarkdownReader
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.vector_stores import SimpleVectorStore
from pydantic import BaseModel, Field

from ..args.env import Env


class Api:
    def __init__(self, env: Env):
        self.env = env

    def get_service_context(self) -> ServiceContext:
        llm = AzureChatOpenAI(
            temperature=0,
            azure_deployment=self.env.azure_open_ai_model_deploy_name,
            model=self.env.azure_open_ai_model_name,
            azure_endpoint=self.env.azure_open_ai_endpoint,
            api_key=self.env.azure_open_ai_key,
            openai_api_type="azure",
            api_version=self.env.azure_open_ai_version,
        )
        llm_predictor = LLMPredictor(llm=llm)

        embedding_llm = LangchainEmbedding(
            AzureOpenAIEmbeddings(
                model=self.env.azure_open_ai_embedding_model_name,
                azure_deployment=self.env.azure_open_ai_embedding_model_deploy_name,
                azure_endpoint=self.env.azure_open_ai_endpoint,
                api_key=self.env.azure_open_ai_key,
                openai_api_type="azure",
                api_version=self.env.azure_open_ai_version,
            ),
            embed_batch_size=1,
        )

        return ServiceContext.from_defaults(
            llm_predictor=llm_predictor,
            embed_model=embedding_llm,
        )

    def save_notion_pages(self, documents: List[Document]) -> None:
        service_context = self.get_service_context()
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore(),
            vector_store=SimpleVectorStore(),
            index_store=SimpleIndexStore(),
        )

        index = GPTVectorStoreIndex.from_documents(
            documents=documents,
            service_context=service_context,
            storage_context=storage_context,
        )
        index.storage_context.persist(persist_dir=self.env.storage_context_tmp_dir)

    def ask(self, query: str) -> None:
        query = query + (
            "REST API を使って GitHub にレビュー内容を POST したいので、"
            "エラーにならないように出力内容は指定された json schema の制約に従ってください。"
        )
        print("query: \n" + query, file=sys.stderr)
        service_context = self.get_service_context()
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir
            ),
            vector_store=SimpleVectorStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir,
                namespace="default",
            ),
            index_store=SimpleIndexStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir
            ),
        )
        index = load_index_from_storage(
            service_context=service_context,
            storage_context=storage_context,
        )

        reader = MarkdownReader()

        for doc in reader.load_data(file=Path("./inputs/pr_summary.md")):
            index.insert(doc)

        qe = index.as_query_engine(
            output_cls=Response,
        )
        try:
            response = qe.query(query)
            response_str = str(response)
            if response_str.startswith("ValueError: Could not extract json string from output: "):
                self.print_comment(response_str)
                return

            print(response)
        except Exception as e:
            self.print_comment(str(e))

    def print_comment(self, body: str) -> None:
        print(json.dumps({"body": body, "event": "COMMENT", "comments": []}))


class Comment(BaseModel):
    path: str = Field(
        ...,
        description=("The relative path to the file that necessitates a review comment."),
    )
    position: int = Field(
        ...,
        description=(
            "The position in the diff where you want to add a review comment. "
            "Note this value is not the same as the line number in the file. This value equals the "
            'number of lines down from the first "@@" hunk header in the file you want to add a '
            'comment. The line just below the "@@" line is position 1, the next line is '
            "position 2, and so on. The position in the diff continues to increase through "
            "lines of whitespace and additional hunks until the beginning of a new file."
            "If this value is specified for a line that does not actually exist, "
            "an error will result, so it must be set so that it does not exceed that range."
        ),
    )
    body: str = Field(
        ...,
        description="Text of the review comment.",
    )


class Response(BaseModel):
    body: str = Field(
        ...,
        description=(
            "Required when using REQUEST_CHANGES or COMMENT for the event parameter."
            "The body text of the pull request review."
        ),
    )
    event: str = Field(
        ...,
        description=(
            "The review action you want to perform. The review actions "
            "include: APPROVE, REQUEST_CHANGES, or COMMENT. By leaving this blank, "
            "you set the review action state to PENDING, which means "
            "you will need to submit the pull request review when you are ready."
            "This field should always be set to the value COMMENT."
        ),
    )

    comments: List[Comment] = Field(
        ...,
        description="Specify the location, destination, and contents of the draft review comment.",
    )
