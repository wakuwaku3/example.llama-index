import os


class Env:
    def __init__(self) -> None:
        # self.azure_open_ai_key = os.environ["AZURE_OPEN_AI_KEY"]
        # self.azure_open_ai_endpoint = os.environ["AZURE_OPEN_AI_ENDPOINT"]
        # self.azure_open_model_deploy_name = os.environ["AZURE_OPEN_MODEL_DEPLOY_NAME"]
        self.notion_api_key = os.environ["NOTION_API_KEY"]

    def validate(self) -> None:
        # assert self.azure_open_ai_key is not None
        # assert self.azure_open_ai_endpoint is not None
        # assert self.azure_open_model_deploy_name is not None
        assert self.notion_api_key is not None


def get_env() -> Env:
    e = Env()
    e.validate()
    return e
