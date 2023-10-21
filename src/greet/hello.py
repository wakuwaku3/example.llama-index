class Greeter:
    def __init__(self, name: str):
        self.name = name

    def say(self) -> str:
        return f"Hello {self.name}"
