from character import Enemy, Hero
from weapon import iron_sword, short_bow

hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="enemy", health=100, weapon=short_bow)

while True:
  hero.attack(enemy)
  enemy.attack(hero)

  print(f"Health of {hero.name}: {hero.health}")
  print(f"Health of {enemy.name}: {enemy.health}")


  hero.drop()
  
  input()