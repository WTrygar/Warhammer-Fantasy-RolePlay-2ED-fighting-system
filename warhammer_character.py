#imports
from abc import ABC
from random import randint

from health_bar import HealthBar
from warhammer_weapons import fists, hochlandLongRifle

enemies = []

class Character(ABC):
  health_bar: HealthBar
  
  def __init__(self,
               #name, race and class of character
               name: str,
               race: str,
               career: str,

               #main profile
               weapon_skill: int,
               ballistic_skill: int,
               strength: int,
               toughness: int,
               agility: int,
               intelligence: int,
               will_power: int,
               fellowship: int,

               #secondary profile
               attacks: int,
               health_max: int,
               health: int,
               strength_bonus: int,
               toughness_bonus: int,
               movement: int,
               magic: int,
               insanity_points: int,
               fate_points: int,

               #bonus stats
               weapons: list,
               items: list,
               spells: set,

               ) -> None:
    self.name = name
    self.race = race
    self.career = career
    self.weapon_skills = weapon_skill
    self.ballistic_skills = ballistic_skill
    self.strength = strength
    self.toughness = toughness
    self.agility = agility
    self.intelligence = intelligence
    self.will_power = will_power
    self.fellowship = fellowship
    self.attacks = attacks
    self.health_max = health_max
    self.health = health
    self.strength_bonus = strength_bonus
    self.toughness_bonus = toughness_bonus
    self.movement = movement
    self.magic = magic
    self.insanity_points = insanity_points
    self.fate_points = fate_points
    self.weapons = weapons
    self.items = items
    self.spells = spells
  
  @property
  def alive(self) -> bool:
    return self.health > 0
  
  @staticmethod
  def roll_event(stat_chance: int) -> bool:
    rolled_event = randint(1, 100)
    return rolled_event <= stat_chance
  
  def attack(self, target) -> None:
    if not self.alive:
      print(f"{self.name} has fallen in battle...")
      return
    
    dmg = self.picked_weapon.damage

    target.get_damaged(dmg, self)
    
  def get_damaged(self, dmg: int, attacker) -> None:
    self.health -= dmg
    self.health = max(self.health, 0)
    self.health_bar.update()
    print(f"{attacker.name} dealt {dmg} damage to {self.name} with {attacker.picked_weapon.name}")


class PlayerCharacter(Character):
  def __init__(self, name, race, career, weapon_skill, ballistic_skill, strength, toughness, agility, intelligence, will_power, fellowship, attacks, health_max, health, movement, magic, insanity_points, fate_points, weapons, items, spells):
    super().__init__(name = name,
                     race = race,
                     career = career,
                     weapon_skill = weapon_skill,
                     ballistic_skill = ballistic_skill,
                     strength = strength,
                     toughness = toughness,
                     agility = agility,
                     intelligence = intelligence,
                     will_power = will_power,
                     fellowship = fellowship,
                     attacks = 1,
                     health_max = health_max,
                     health = health,
                     strength_bonus = 0,
                     toughness_bonus = 0,
                     movement = movement,
                     magic = 0,
                     insanity_points = 0,
                     fate_points = 0,
                     weapons = [],
                     items = [],
                     spells = [])
    
    self.strength_bonus = strength // 10
    self.toughness_bonus = toughness // 10

    self.picked_weapon = weapons[0]
    self.health_bar = HealthBar(self, color="green")

  
    


class EnemyCharacter(Character):
  def __init__(self, name, race, career, weapon_skill, ballistic_skill, strength, toughness, agility, intelligence, will_power, fellowship, attacks, health_max, health, movement, magic, insanity_points, fate_points, weapons, items, spells):
    super().__init__(name = name,
                     race = race,
                     career = career,
                     weapon_skill = weapon_skill,
                     ballistic_skill = ballistic_skill,
                     strength = strength,
                     toughness = toughness,
                     agility = agility,
                     intelligence = intelligence,
                     will_power = will_power,
                     fellowship = fellowship,
                     attacks = 1,
                     health_max = health_max,
                     health = health,
                     strength_bonus = 0,
                     toughness_bonus = 0,
                     movement = movement,
                     magic = 0,
                     insanity_points = insanity_points,
                     fate_points = fate_points,
                     weapons = [],
                     items = [],
                     spells = ())
    
    self.strength_bonus = strength // 10
    self.toughness_bonus = toughness // 10

    self.picked_weapon = weapons[0]
    self.health_bar = HealthBar(self, color="red")

    enemies.append(self)

#  IDEAS FOR RACES AND CAREERS ADDING BONUS STATS AND DATA TO CHARACTERS

# bonus_stat_dict = {
#   "elf" : {
#     "strght": 0,
#     "dex": 5,
#     "hp": 2
#   },
#   "orc":  {
#     "strght": 4,
#     "dex": 0,
#     "hp": 3
#   },
#   "knight": {
#     "strght": 4,
#     "dex": 0,
#     "hp": 3
#   },
#   "ranger":  {
#     "strght": 0,
#     "dex": 5,
#     "hp": 2
#   }
# }


# class BonusStats():
#   strght: int
#   dex: int
#   hp: int
#   def __init__(self, stat_dict: dict):