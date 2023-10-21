from greet.hello import Greeter


class TestGreeter:
    def test_greeter_say(self) -> None:
        greeter = Greeter("World")
        assert greeter.say() == "Hello World"

    def test_greeter_name(self) -> None:
        greeter = Greeter("GitHub Copilot")
        assert greeter.name == "GitHub Copilot"
