import sys

from .env import Env, get_env


class Args:
    def __init__(self, args: list[str], env: Env) -> None:
        self.env = env
        self.args = args
        self.notion_database_id = args[1]

    def validate(self) -> None:
        assert self.env is not None
        assert self.notion_database_id is not None
        self.env.validate()


def get_args() -> Args:
    a = Args(sys.argv, get_env())
    a.validate()
    return a
