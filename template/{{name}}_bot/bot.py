from encodings import utf_8
from pathlib import Path
from typing import Callable
from threading import Timer

import os
import logging

from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from pytz import timezone as tz

from {{ name }}_bot.config import {{ name_pascal_case }}BotConfig
from {{ name }}_bot.cron_machine import CronMachine

UTF_8 = utf_8.getregentry().name


class {{ name_pascal_case }}Bot:
    ENV_TOKEN_VAR = "{{ name.upper() }}_BOT_TOKEN"

    def __init__(self, config: {{ name_pascal_case }}BotConfig):
        token = os.getenv(self.ENV_TOKEN_VAR)
        if not token:
            raise EnvironmentError(f"Token not found in {self.ENV_TOKEN_VAR}")

        self.updater = Updater(
            token=token,
            use_context=True,
        )
        dispatcher = self.updater.dispatcher

        echo_handler = MessageHandler(Filters.text, self.echo)
        dispatcher.add_handler(echo_handler)

        self.bot: Bot = self.updater.bot

        self.cron_machine = CronMachine(tz=tz(config.cron_machine.timezone))

    def run(self):
        self.updater.start_polling()
        self.cron_machine.start()

    def echo(self, update: Update, context: CallbackContext) -> None:
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=update.message.text)

    def stop(self) -> None:
        self.updater.stop()
        self.cron_machine.stop()
