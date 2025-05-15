# imports
import os

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

      hero.attack(enemy)
      enemy.attack(hero)

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