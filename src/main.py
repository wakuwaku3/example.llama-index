from greet.hello import Greeter
from log.logger import Logger


def main() -> None:
    greeter = Greeter("wakuwaku3")
    logger = Logger()
    logger.write_green(greeter.say())


if __name__ == "__main__":
    main()
