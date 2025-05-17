#here's an idea, for a class that as a default has random values, so we could generate characters faster

#imports
from abc import ABC
from random import randint

from health_bar import HealthBar


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

              #  secondary profile
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

snorri = Character(name = "Snorri",
                         race = "Dwarf",
                         career = "Engineer",
                         )

print(f"Name: {snorri.name}")
print(f"Race: {snorri.race}")
print(f"Career: {snorri.career}")
print(f"Weapon Skills (WS): {snorri.weapon_skills}")
print(f"Ballistic Skills (BS): {snorri.ballistic_skills}")
print(f"Strength (S): {snorri.strength}")
print(f"Toughness (T): {snorri.toughness}")
print(f"Agility (Ag): {snorri.agility}")
print(f"Intelligence (Int): {snorri.intelligence}")
print(f"Willpower (WP): {snorri.will_power}")
print(f"Fellowship (Fel): {snorri.fellowship}")
print(f"Attacks (A): {snorri.attacks}")
print(f"Maximum health (Wounds - W): {snorri.health_max} and current: {snorri.health}")
print(f"Strength Bonus (SB): {snorri.strength_bonus} (SB == S // 10)")
print(f"Toughness Bonus (TB): {snorri.toughness_bonus} (TB == T // 10)")
print(f"Movement (M): {snorri.movement}")
print(f"Magic (Mag): {snorri.magic}")  
print(f"Insanity Points (IP): {snorri.insanity_points}")
print(f"Fate Points (FP): {snorri.fate_points}")
print(f"Weapons: {snorri.weapons}")
