import json
import sys
import uuid
from typing import Any, Dict, List


class Args:
    def __init__(self, args: list[str]) -> None:
        self.args = args
        self.action = args[1]
        assert self.action in {"save", "review"}

        if self.action == "save":
            if len(self.args) > 2:
                self.notion_database_id = args[2]
                with open("./inputs/notion_database_query.json", encoding="utf-8") as f:
                    self.notion_query_json = f.read()
            else:
                self.notion_database_id = None
            with open("./inputs/notion_document_ids.json", encoding="utf-8") as f:
                self.notion_document_ids_json = f.read()
            assert self.notion_database_id is not None or self.notion_document_ids_json is not None

    def is_save(self) -> bool:
        return self.action == "save"

    def get_notion_query(self) -> Dict[str, Any]:
        if self.notion_query_json is None:
            return {}
        return json.loads(self.notion_query_json)

    def notion_document_ids(self) -> List[str]:
        ids: List[str] = []
        if self.notion_document_ids_json is not None:
            for doc_id in json.loads(self.notion_document_ids_json):
                ids.append(str(uuid.UUID(doc_id)))
        return ids

    def get_prompt(self) -> str:
        with open("./inputs/prompt.md", encoding="utf-8") as f:
            s = f.read()
            return s


def get_args() -> Args:
    a = Args(sys.argv)
    return a
