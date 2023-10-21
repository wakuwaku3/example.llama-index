import json
import sys
from typing import Any, Dict


class Args:
    def __init__(self, args: list[str]) -> None:
        self.args = args
        self.action = args[1]
        assert self.action in {"save", "review"}

        if self.action == "save":
            self.notion_database_id = args[2]
            self.notion_query_json = args[3]
            assert self.notion_database_id is not None
        else:
            self.review_query = args[2]
            assert self.review_query is not None

    def is_save(self) -> bool:
        return self.action == "save"

    def get_notion_query(self) -> Dict[str, Any]:
        if self.notion_query_json is None:
            return {}
        return json.loads(self.notion_query_json)


def get_args() -> Args:
    a = Args(sys.argv)
    return a
