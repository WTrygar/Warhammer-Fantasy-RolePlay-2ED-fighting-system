# imports
import os

from character import Enemy, Hero, enemies
from weapon import iron_sword, short_bow

# setup
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="enemy", health=100, weapon=short_bow)

# game class
class Game:
  def __init__(self):
    self.running = True

  @staticmethod
  def spawn_enemy() -> Enemy:
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
      os.system("cls")

      hero.attack(enemy)
      enemy.attack(hero)

      hero.health_bar.draw()
      enemy.health_bar.draw()

      input()

      self.running = hero.health > 0

      if enemy.health <= 0:
        enemies.pop(0)
        enemy = self.spawn_enemy()
    input("GAME OVER")
    exit()

# game loop
if __name__ == "__main__":
  game = Game()
  game.run