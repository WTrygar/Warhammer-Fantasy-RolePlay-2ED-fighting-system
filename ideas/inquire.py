import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

actions = [
    inquirer.List(
        "action",
        message="What do You want to do?",
        choices=["attack", "switch weapon", "use item", "check_character"],
    ),
]

answers = inquirer.prompt(actions)
term = answers['action']
match term:
  case "attack":
    print(f"We have attacked!")
  case "switch weapon":
    print(f"We have switched our weapon!")
  case "use item":
    print(f"pick item that You want to use!")
  case "check_character":
    print(f"choose a character that You want to check!")

pprint(answers)
