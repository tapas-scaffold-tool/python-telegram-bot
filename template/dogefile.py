from subprocess import run
from pathlib import Path

import os

from dogebuild import make_mode, task


make_mode()

IMAGE_NAME = "{{ name_kebab_case }}-bot"
ENV_TOKEN_VAR = "{{ name.upper() }}_BOT_TOKEN"

BUILD_DIR = Path("./build")


@task
def build_docker():
    run(["docker", "build", "-t", IMAGE_NAME, "."], check=True)


@task(depends=["build_docker"])
def run_docker():
    token = os.getenv(ENV_TOKEN_VAR)
    run(["docker", "run", "-e", f"{ENV_TOKEN_VAR}={token}", IMAGE_NAME], check=True)


@task(depends=["build_docker"])
def build_tar():
    BUILD_DIR.mkdir(exist_ok=True)
    run(["docker", "save", "--output", f"{BUILD_DIR / (IMAGE_NAME + '.tar')}", IMAGE_NAME])
