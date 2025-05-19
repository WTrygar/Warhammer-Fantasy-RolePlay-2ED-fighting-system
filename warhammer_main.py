# imports
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

from warhammer_character import (EnemyCharacter, all_characters, enemies,
                                 playable_characters)
from warhammer_character_list import helmut
from warhammer_weapons import fist, hochlandLongRifle

# setup
heroes = sorted(playable_characters, key=lambda x: x.agility, reverse=True)
characters = sorted(all_characters, key=lambda x: x.agility, reverse=True)


# game class
class Game:
  index = 0
  def __init__(self):
    self.running = True
    
  @staticmethod  
  def clear():
    os.system("cls")

  @staticmethod 
  def spawn_enemy() -> EnemyCharacter:
    Game.clear
    if enemies:
      enemy = enemies[0]
      input(f"Spawning {enemy.name}... ")
      return enemy
    else:
      input("YOU WIN")
      exit()

  @staticmethod
  def check_index() -> None:
    if Game.index + 1 >= len(all_characters):
      Game.index = 0
    else:
      Game.index += 1
    return

  def run(self):
    enemy = self.spawn_enemy()
    while self.running:
      Game.clear()
      print(f"----- {characters[Game.index]} Turn -----")
      actions = [
        inquirer.List(
          "action",
          message="What do You want to do?",
          choices=["standard attack", "nothing"],
        ),
      ]
      answers = inquirer.prompt(actions)
      term = answers['action']
      match term:
        case "standard attack":
          pick_target = [
            inquirer.List(
              "target",
              message="Who's your target?",
              choices=[character for character in characters],
            ),
          ]
          answers_2 = inquirer.prompt(pick_target)
          term = answers_2["target"]
          characters[Game.index].standard_attack(characters[characters.index(term)])
          for i in range(len(characters)):
            characters[i].health_bar.draw()
          Game.check_index()
          input()
        case "nothing":
          print(f"You did nothing")
          for i in range(len(characters)):
            characters[i].health_bar.draw()
          Game.check_index()
          input()

      self.running = heroes[0].alive

      if not enemy.alive:
        enemies.pop(0)
        enemy = self.spawn_enemy()
    input("GAME OVER")
    exit()

# game loop
if __name__ == "__main__":
  # print(heroes)
  game = Game()
  game.run()