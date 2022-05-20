from dataclasses import dataclass
from yaml import load, SafeLoader
from pathlib import Path

from marshmallow_dataclass import class_schema


@dataclass
class CronMachineConfig:
    timezone: str


@dataclass
class {{ name_pascal_case }}BotConfig:
    cron_machine: CronMachineConfig


@dataclass
class {{ name_pascal_case }}BotAppConfig:
    bot: {{ name_pascal_case }}BotConfig


{{ name_pascal_case }}BotConfigSchema = class_schema({{ name_pascal_case }}BotAppConfig)


def load_config(file: Path) -> {{ name_pascal_case }}BotAppConfig:
    return {{ name_pascal_case }}BotConfigSchema().load(
        load(file.read_text(), Loader=SafeLoader)
    )
