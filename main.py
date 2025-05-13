# imports
import os

from character import Enemy, Hero
from weapon import iron_sword, short_bow

# setup
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="enemy", health=100, weapon=short_bow)

# game loop
while True:
  os.system("cls")
  hero.attack(enemy)
  enemy.attack(hero)

  hero.health_bar.draw()
  enemy.health_bar.draw()

  # hero.drop()
  
  input()