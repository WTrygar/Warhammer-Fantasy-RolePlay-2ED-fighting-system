import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

actions = [
    inquirer.List(
        "action",
        message="What do You want to do?",
        choices=["attack", "switch weapon", "use item", "check_other"],
    ),
]

answers = inquirer.prompt(actions)

pprint(answers)