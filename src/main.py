from args.args import get_args
from llama_index_wrapper.notion import Notion


def main() -> None:
    args = get_args()
    print(args.notion_database_id)
    print(args.env.notion_api_key)
    notion = Notion(args)
    ids = notion.get_ids(
        {"filter": {"or": [{"property": "status", "select":{"equals": "approved"}}, {"property": "status", "select":{"equals": "posted"}}]}}
    )
    print(ids)


if __name__ == "__main__":
    main()
