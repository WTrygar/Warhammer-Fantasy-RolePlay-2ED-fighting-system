# imports
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

from warhammer.character import (EnemyCharacter, all_characters, enemies,
                                 playable_characters)
from warhammer.character_list import helmut
from warhammer.weapons import fist, hochlandLongRifle

# setup
heroes = sorted(playable_characters, key=lambda x: x.agility, reverse=True)
characters = sorted(all_characters, key=lambda x: x.agility, reverse=True)
characters_static = sorted(all_characters, key=lambda x: x.agility, reverse=True)

dead_enemies_checker = sorted(enemies, key=lambda x: x.agility, reverse=True)
dead_heroes_checker = sorted(playable_characters, key=lambda x: x.agility, reverse=True)

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
    Game.clear()
    

  @staticmethod
  def check_index() -> None: #function that skip dead characters turns
    while characters_static[Game.index].health == 0:
      print(f"DEAD current value of index: {Game.index}")
      if Game.index == 0:
        Game.index += 1
        print(f"DEAD index was 0, hence increment: {Game.index}")
      elif Game.index + 1 >= len(all_characters):
        Game.index = 0
        print(f"DEAD index would get out of range, so we set it to 0: {Game.index}")
      else:
        Game.index += 1
        print(f"DEAD not zero increment: {Game.index}")
      print(characters_static[Game.index])
    if Game.index + 1 >= len(all_characters):
      Game.index = 0
      while characters_static[Game.index].health == 0:
        print(f"DEAD current value of index: {Game.index}")
        if Game.index == 0:
          Game.index += 1
          print(f"DEAD index was 0, hence increment: {Game.index}")
        elif Game.index + 1 >= len(all_characters):
          Game.index = 0
          print(f"DEAD index would get out of range, so we set it to 0: {Game.index}")
        else:
          Game.index += 1
          print(f"DEAD not zero increment: {Game.index}")
        print(characters_static[Game.index])
      print(f"NOT DEAD out of bounds: {Game.index}")
    elif characters_static[Game.index].health != 0:
      print(characters_static[Game.index])
      Game.index += 1
      print(f"NOT DEAD increment: {Game.index}")
    return

  def run(self):
    enemy = self.spawn_enemy()
    while self.running:
      Game.clear()
      print(f"----- {characters_static[Game.index]} Turn -----")
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
          characters_static[Game.index].standard_attack(characters[characters.index(term)])
          
          for i in range(len(heroes)):
            heroes[i].health_bar.draw()
          
          for i in range(len(dead_enemies_checker)):
            dead_enemies_checker[i].health_bar.draw()
            
          if characters[characters.index(term)].health == 0:
            if isinstance(characters[characters.index(term)], EnemyCharacter):
              dead_enemies_checker.remove(term)
            else:
              dead_heroes_checker.remove(term)
            characters.remove(term)
            print(dead_enemies_checker)
            print(characters)
          Game.check_index()
          input()
        case "nothing":
          print(f"You did nothing")
          for i in range(len(characters)):
            characters[i].health_bar.draw()
          Game.check_index()
          input()

      self.running = len(dead_heroes_checker) > 0
      if dead_enemies_checker:
        print('')
      else:
        input("YOU WIN")
        exit()
    input("GAME OVER")
    exit()

# game loop
if __name__ == "__main__":
  # print(heroes)
  game = Game()
  game.run()