# imports
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer

from warhammer.character import (Character, EnemyCharacter, PlayerCharacter,
                                 all_characters, enemies, playable_characters)
from warhammer.character_list import helmut
from warhammer.weapons import fist, hochlandLongRifle


# game class
class Game:
  """class that handles the battle.
  vars:
  - index - int that keeps track which character's turn is it. Increments after the end of characters turn. Resets back to zero when reached the end of the characters queue.
  - action_counter - int that keeps track how many "actions" can character make in it's turn. Resets back to default value after the end of character's turn.
  """

  index = 0
  action_counter = 4

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
  def check_index(self) -> None: 
    """function that keeps track of which character turn it is, skips those that are dead"""
    # implement action counter
    if Game.action_counter == 0:
      Game.action_counter = 4
      if Game.index + 1 >= len(self.characters_static):
        Game.index = 0
        while self.characters_static[Game.index].health == 0:
          Game.index += 1

      else:
        Game.index += 1
        while self.characters_static[Game.index].health == 0:
          if Game.index + 1 > len(self.characters_static):
            Game.index = 0
          else:
            Game.index += 1
    return

  def run(self):
    """function that handles the choice of chararcter actions and the targets of these actions if needed"""
    print('')
    print('')
    print('')
    print('')
    print('')
    for i in range(len(self.characters)):
      self.characters[i].health_bar.draw()
    input()

    while self.running:
      # Game.clear()
      print(f"----- {Game.index + 1}. {self.characters_static[Game.index]}'s turn -----")
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
          game.clear()
          print('')
          print('')
          print('')
          print('')
          print('')
          for i in range(len(self.characters)):
            self.characters[i].health_bar.draw()
          print('')
          pick_target = [
            inquirer.List(
              "target",
              message="Who's your target?",
              choices=[character for character in self.characters],
            ),
          ]
          answers_2 = inquirer.prompt(pick_target)
          term = answers_2["target"]
          game.clear()
          print('')
          self.characters_static[Game.index].standard_attack(self.characters[self.characters.index(term)])
          
          for i in range(len(self.characters)):
            self.characters[i].health_bar.draw()
            
          if self.characters[self.characters.index(term)].health == 0:
            if isinstance(self.characters[self.characters.index(term)], EnemyCharacter):
              self.dead_enemies_checker.remove(term)
            else:
              self.dead_heroes_checker.remove(term)
            self.characters.remove(term)
            # print(self.dead_enemies_checker)
            # print(self.characters)
          Game.action_counter -= 2
          Game.check_index(self)
          print('')
          input("Press any key to proceed")
          
        case "nothing - skip turn":
          game.clear()
          print(f"{self.characters_static[Game.index]} did nothing and skipped it's turn")
          print('')
          print('')
          print('')
          print('')
          for i in range(len(self.characters)):
            self.characters[i].health_bar.draw()
          Game.action_counter = 0
          Game.check_index(self)
          print('')
          input("Press any key to proceed")

      self.running = len(self.dead_heroes_checker) > 0
      if self.dead_enemies_checker:
        print('')
      else:
        input("YOU WIN")
        exit()
    input("GAME OVER")
    exit()

  def menu(self):
    while self.running:
      options = [
        inquirer.List(
          "option",
          message="Warhammer Fantasy Roleplay 2nd edition Battle Tracker",
          choices=["Battle", "Create Character - Not yet available", "Update Character - Not yet available", "Update Teams"],
        ),
      ]
      answers = inquirer.prompt(options)
      term = answers['option']

      match term:
        case "Battle":
          game.clear()
          game.run()

        case "Create Character - Not yet available":
          options = [
            inquirer.List(
              "option",
              message="Do You want to create Hero or Enemy?",
              choices=["Hero", "Enemy"],
            ),
          ]
          answers = inquirer.prompt(options)
          term = answers['option']
          match term:
            case "Hero":
              name = input("What's the name of the character: ")
              character = PlayerCharacter.create_playable_character(name)
            case "Enemy":
              name = input("What's the name of the character: ")
              character = EnemyCharacter.create_enemy_character(name)

        case "Update Character - Not yet available":
          game.menu()

        case "Update Teams":
          options = [
            inquirer.List(
              "option",
              message="Which team would You like to rearrange?",
              choices=["Heroes", "Enemies"],
            ),
          ]
          answers = inquirer.prompt(options)
          term = answers['option']

          match term:
            case "Heroes":
              questions = [
                inquirer.Checkbox(
                  "Heroes",
                  message="Arrange party of heroes",
                  choices=[hero for hero in playable_characters],
                ),
              ]
              answers = inquirer.prompt(questions)
              print(answers)
              self.heroes = answers["Heroes"]
              self.dead_heroes_checker = answers["Heroes"]
              self.characters = [*self.heroes, *self.dead_enemies_checker]
              self.characters_static = [*self.heroes, *self.dead_enemies_checker]
              # print(heroes)
              game.menu()

            case "Enemies":
              questions = [
                inquirer.Checkbox(
                  "Enemies",
                  message="Arrange party of enemies",
                  choices=[enemy for enemy in enemies],
                ),
              ]
              answers = inquirer.prompt(questions)
              print(answers)
              self.dead_enemies_checker = answers["Enemies"]
              self.characters = [*self.heroes, *self.dead_enemies_checker]
              self.characters_static = [*self.heroes, *self.dead_enemies_checker]
              game.menu()


# game loop
if __name__ == "__main__":
  game = Game()
  game.clear()
  game.menu()