import os
import re

from tapas.tools import prompt_bool, init_git_repo, prompt_str, prompt_license, generate_license_file
from tapas.context import ContextHolder


def snake_case_to_pascal_case(value: str) -> str:
    return ''.join([w.title() for w in value.split("_")])

def snake_case_to_kebab_case(value: str) -> str:
    return value.replace("_", "-")

# Require from user to enter parameters in this function
def ask():
    name_pattern = "[a-z][a-z_]*"
    prompt_str("name", prompt_string=f"Enter name ({name_pattern}): ", validators=[
        lambda name: None if re.match(f"^{name_pattern}$", name) else f"Name {name} doesn't match {name_pattern}.",
    ])
    ContextHolder.CONTEXT.put("name_pascal_case", snake_case_to_pascal_case(ContextHolder.CONTEXT.get("name")))
    ContextHolder.CONTEXT.put("name_kebab_case", snake_case_to_kebab_case(ContextHolder.CONTEXT.get("name")))

    # Remove if no need to control README.md
    prompt_bool('readme', default_value="y", prompt_string="Create README.md file? [Y/n]: ")

    # Remove if no need in LICENSE file
    prompt_license()

    # Remove if no need in git repo init control
    prompt_bool('git', default_value="y", prompt_string="Init git repository? [Y/n]: ")

# Perform additional actions after generation in this function
def post_init(readme: bool, license: str, git: bool):
    # Remove if no need to control README.md
    if not readme:
        os.remove('README.md')

    # Remove if no need in LICENSE file
    generate_license_file(license)

    # Remove if no need in git repo init control
    if git:
        init_git_repo()
