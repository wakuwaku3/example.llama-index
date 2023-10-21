from typing import Any, Dict, List

from llama_index import Document, NotionPageReader

from args.env import Env


class Notion:
    def __init__(self, env: Env) -> None:
        self.env = env
        self.reader = NotionPageReader(integration_token=env.notion_api_key)

    def get_documents(self, notion_database_id: str, query_dict: Dict[str, Any]) -> List[Document]:
        ids = self.reader.query_database(notion_database_id, query_dict)
        return self.reader.load_data(ids)
