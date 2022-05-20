import logging
import signal
from pathlib import Path

from {{ name }}_bot.bot import {{ name_pascal_case }}Bot
from {{ name }}_bot.config import load_config


class {{ name_pascal_case }}BotApp:
    CONFIG_FILE = "config.yaml"

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s\t%(threadName)s\t%(name)s\t%(levelname)s\t%(message)s"
        )
        config = load_config(Path() / self.CONFIG_FILE)
        self.bot = {{ name_pascal_case }}Bot(config.bot)

        signal.signal(signal.SIGINT, self.exit)

    def main(self) -> int:
        self.bot.run()
        return 0

    def exit(self, sig, frame):
        self.bot.stop()
