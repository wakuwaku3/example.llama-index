from args.args import Args, get_args
from args.env import Env
from llama_index_wrapper.api import Api
from llama_index_wrapper.notion import Notion
from storage.storage import Storage
from zip.zip import compress, decompress


def main() -> None:
    args = get_args()
    env = Env(args)
    if args.is_save():
        save_indexes(args, env)
    else:
        review(args, env)


def save_indexes(args: Args, env: Env) -> None:
    notion = Notion(env)
    api = Api(env)
    storage = Storage(env)

    documents = notion.get_documents(
        args.notion_database_id,
        args.get_notion_query(),
        args.notion_document_ids(),
    )
    print(documents)
    api.save_notion_pages(documents)
    compress(env.storage_context_tmp_dir, env.storage_context_tmp_dir)
    storage.upload_from_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        env.google_index_file_name,
    )


def review(args: Args, env: Env) -> None:
    storage = Storage(env)
    storage.download_to_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        env.google_index_file_name,
    )
    decompress(env.storage_context_tmp_zip, env.storage_context_tmp_dir)
    api = Api(env)
    api.ask(args.get_prompt())


if __name__ == "__main__":
    main()
