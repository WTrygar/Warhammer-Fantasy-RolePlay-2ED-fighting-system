# imports
import os
import sys

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

from warhammer_character import EnemyCharacter, enemies
from warhammer_character_list import helmut
from warhammer_weapons import fists, hochlandLongRifle

# setup
hero = helmut

# game class
class Game:
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

  def run(self):
    enemy = self.spawn_enemy()
    while self.running:
      Game.clear()

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
          print(f"We have attacked!")
          hero.standard_attack(enemy)
          enemy.standard_attack(hero)
          hero.health_bar.draw()
          enemy.health_bar.draw()
          input()
        case "nothing":
          print(f"You did nothing")
          enemy.standard_attack(hero)
          hero.health_bar.draw()
          enemy.health_bar.draw()
          input()

      self.running = hero.alive

      if not enemy.alive:
        enemies.pop(0)
        enemy = self.spawn_enemy()
    input("GAME OVER")
    exit()

# game loop
if __name__ == "__main__":
  game = Game()
  game.run()