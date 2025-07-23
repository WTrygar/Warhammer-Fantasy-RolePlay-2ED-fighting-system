# imports
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

from warhammer.character import (EnemyCharacter, all_characters, enemies,
                                 playable_characters)
from warhammer.character_list import helmut
from warhammer.weapons import fist, hochlandLongRifle

# list of all playable characters
heroes = sorted(playable_characters, key=lambda x: x.agility, reverse=True)

# list of all characters (mutable)
characters = sorted(all_characters, key=lambda x: x.agility, reverse=True)

# list of all characters (unmutable)
characters_static = sorted(all_characters, key=lambda x: x.agility, reverse=True)

# list of all enemy characters to check if all are dead
dead_enemies_checker = sorted(enemies, key=lambda x: x.agility, reverse=True)

# list of all playable characters to check if all are dead
dead_heroes_checker = sorted(playable_characters, key=lambda x: x.agility, reverse=True)

# game class
class Game:
  """class that handles the battle.
  vars:
  - index - int that keeps track which character's turn is it. Increments after the end of characters turn. Resets back to zero when reached the end of the characters queue.
  - action_counter - int that keeps track how many "actions" can character make in it's turn. Resets back to default value after the end of character's turn.
  """
  index = 0
  action_counter = 4
  def __init__(self):
    self.running = True

    
  @staticmethod  
  def clear(): 
    """function that clears the terminal"""
    os.system("cls")

  @staticmethod 
  def spawn_enemy() -> EnemyCharacter: 
    """function that spawns enemy (used previously when fights were 1 vs 1)"""
    Game.clear()
    

  @staticmethod
  def check_index() -> None: 
    """function that keeps track of which character turn it is, skips those that are dead"""
    # implement action counter
    if Game.action_counter == 0:
      Game.action_counter = 4
      if Game.index + 1 >= len(characters_static):
        Game.index = 0
        while characters_static[Game.index].health == 0:
          Game.index += 1

      else:
        Game.index += 1
        while characters_static[Game.index].health == 0:
          if Game.index + 1 > len(characters_static):
            Game.index = 0
          else:
            Game.index += 1
    return

  def run(self):
    """function that handles the choice of chararcter actions and the targets of these actions if needed"""
    for i in range(len(characters)):
      characters[i].health_bar.draw()
    input()

    while self.running:
      Game.clear()
      print(f"----- {Game.index + 1}. {characters_static[Game.index]}'s turn -----")
      print(f" Remaining actions: {Game.action_counter}")

      actions = [
        inquirer.List(
          "action",
          message="What do You want to do?",
          choices=["standard attack - 2", "nothing - skip turn"],
        ),
      ]
      answers = inquirer.prompt(actions)
      term = answers['action']

      match term:
        case "standard attack - 2":
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
          
          for i in range(len(characters)):
            characters[i].health_bar.draw()
            
          if characters[characters.index(term)].health == 0:
            if isinstance(characters[characters.index(term)], EnemyCharacter):
              dead_enemies_checker.remove(term)
            else:
              dead_heroes_checker.remove(term)
            characters.remove(term)
            print(dead_enemies_checker)
            print(characters)
          Game.action_counter -= 2
          Game.check_index()
          input()
          
        case "nothing - skip turn":
          print(f"{characters_static[Game.index]} did nothing and skipped it's turn")
          for i in range(len(characters)):
            characters[i].health_bar.draw()
          Game.action_counter = 0
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

  def menu(self):
    Game.clear()
    while self.running:
      

      options = [
        inquirer.List(
          "option",
          message="Warhammer Fantasy Roleplay 2nd edition Battle Tracker",
          choices=["Battle", "Create Character - Not yet available", "Update Character - Not yet available", "Update Teams - Not yet available"],
        ),
      ]
      answers = inquirer.prompt(options)
      term = answers['option']

      match term:
        case "Battle":
          game.run()

        case "Create Character - Not yet available":
          game.menu()

        case "Update Character - Not yet available":
          game.menu()

        case "Update Teams - Not yet available":
          game.menu()


# game loop
if __name__ == "__main__":
  game = Game()
  game.menu()