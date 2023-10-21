from typing import Any, Dict, List

from llama_index import NotionPageReader

from args.args import Args


class Notion:
    def __init__(self, args: Args) -> None:
        self.args = args
        self.reader = NotionPageReader(integration_token=args.env.notion_api_key)

    def get_ids(self, query_dict: Dict[str, Any]) -> List[str]:
        ids = self.reader.query_database(self.args.notion_database_id, query_dict)
        return ids
