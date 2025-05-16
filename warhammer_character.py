#imports
from abc import ABC
from random import randint

from health_bar import HealthBar
from warhammer_weapons import fists, hochlandLongRifle

enemies = []
playable_characters = []

# ----- Parent Class -----
class Character(ABC):
  health_bar: HealthBar
  def __init__(self,
               #name, race and class of character
               name: str,
               race: str,
               career: str,

               #main profile
               weapon_skill: int = None,
               ballistic_skill: int = None,
               strength: int = None,
               toughness: int = None,
               agility: int = None,
               intelligence: int = None,
               will_power: int = None,
               fellowship: int = None,

               #secondary profile
               attacks: int = None,
               health_max: int = None,
               health: int = None,
               strength_bonus: int = None,
               toughness_bonus: int = None,
               movement: int = None,
               magic: int = None,
               insanity_points: int = None,
               fate_points: int = None,

               #bonus stats
               weapons: list = [],
               items: list = [],
               spells: set = (),

               ) -> None:
    self.name = name
    self.race = race
    self.career = career
    self.weapon_skills = weapon_skill if weapon_skill is not None else randint(2, 20)
    self.ballistic_skills = ballistic_skill if ballistic_skill is not None else randint(2, 20)
    self.strength = strength if strength is not None else randint(2, 20)
    self.toughness = toughness if toughness is not None else randint(2, 20)
    self.agility = agility if agility is not None else randint(2, 20)
    self.intelligence = intelligence if intelligence is not None else randint(2, 20)
    self.will_power = will_power if will_power is not None else randint(2, 20)
    self.fellowship = fellowship if fellowship is not None else randint(2, 20)
    self.attacks = attacks if attacks is not None else 1
    self.health_max = health_max if health_max is not None else 1
    self.health = health if health is not None else 1
    self.strength_bonus = strength_bonus
    self.toughness_bonus = toughness_bonus
    self.movement = movement if movement is not None else 1
    self.magic = magic if magic is not None else 0
    self.insanity_points = insanity_points if insanity_points is not None else 0
    self.fate_points = fate_points if fate_points is not None else 0
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
  
  def __repr__(self):
    return f'{self.name}'
  
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

# ----- First Child Class -----
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
                     attacks = attacks,
                     health_max = health_max,
                     health = health,
                     strength_bonus = 0,
                     toughness_bonus = 0,
                     movement = movement,
                     magic = magic,
                     insanity_points = insanity_points,
                     fate_points = fate_points,
                     weapons = weapons,
                     items = items,
                     spells = spells)
    
    self.strength_bonus = strength // 10
    self.toughness_bonus = toughness // 10

    self.picked_weapon = weapons[0]
    self.health_bar = HealthBar(self, color="green")

    playable_characters.append(self)

# -----Second Child Class-----
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
                     attacks = attacks,
                     health_max = health_max,
                     health = health,
                     strength_bonus = 0,
                     toughness_bonus = 0,
                     movement = movement,
                     magic = magic,
                     insanity_points = insanity_points,
                     fate_points = fate_points,
                     weapons = weapons,
                     items = items,
                     spells = spells)
    
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