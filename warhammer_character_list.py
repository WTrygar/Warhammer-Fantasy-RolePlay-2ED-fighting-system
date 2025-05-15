from warhammer_character import Character, EnemyCharacter, PlayerCharacter
from warhammer_weapons import MeleeWeapon, MissileWeapon, Weapon, fists

helmut = PlayerCharacter(name = "Helmut",
                         race = "Human",
                         career = "Bone Picker",
                         weapon_skill = 30,
                         ballistic_skill = 30,
                         strength = 30,
                         toughness = 30,
                         agility = 30,
                         intelligence = 30,
                         will_power = 30,
                         fellowship = 30,
                         attacks = 1,
                         health_max = 12,
                         health = 12,
                         movement = 4,
                         magic = 0,
                         insanity_points = 0,
                         fate_points = 2,
                         weapons = [fists],
                         items = [],
                         spells = ())


archaon = EnemyCharacter(name = "Archaon the Everchosen",
                         race = "Mutant",
                         career = "Everchosen",
                         weapon_skill = 70,
                         ballistic_skill = 30,
                         strength = 60,
                         toughness = 60,
                         agility = 40,
                         intelligence = 60,
                         will_power = 70,
                         fellowship = 50,
                         attacks = 2,
                         health_max = 50,
                         health = 50,
                         movement = 4,
                         magic = 3,
                         insanity_points = 10,
                         fate_points = 3,
                         weapons = [fists],
                         items = [],
                         spells = ())
enemies = []

if __name__ == "__main__":
  print(f"Name: {helmut.name}")
  print(f"Race: {helmut.race}")
  print(f"Career: {helmut.career}")
  print(f"Weapon Skills (WS): {helmut.weapon_skills}")
  print(f"Ballistic Skills (BS): {helmut.ballistic_skills}")
  print(f"Strength (S): {helmut.strength}")
  print(f"Toughness (T): {helmut.toughness}")
  print(f"Agility (Ag): {helmut.agility}")
  print(f"Intelligence (Int): {helmut.intelligence}")
  print(f"Willpower (WP): {helmut.will_power}")
  print(f"Fellowship (Fel): {helmut.fellowship}")
  print(f"Attacks (A): {helmut.attacks}")
  print(f"Maximum health (Wounds - W): {helmut.health_max} and current: {helmut.health}")
  print(f"Strength Bonus (SB): {helmut.strength_bonus} (SB == S // 10)")
  print(f"Toughness Bonus (TB): {helmut.toughness_bonus} (TB == T // 10)")
  print(f"Movement (M): {helmut.movement}")
  print(f"Magic (Mag): {helmut.magic}")  
  print(f"Insanity Points (IP): {helmut.insanity_points}")
  print(f"Fate Points (FP): {helmut.fate_points}")
  print(f" ")
  print(f"Name: {archaon.name}")
  print(f"Race: {archaon.race}")
  print(f"Career: {archaon.career}")
  print(f"Weapon Skills (WS): {archaon.weapon_skills}")
  print(f"Ballistic Skills (BS): {archaon.ballistic_skills}")
  print(f"Strength (S): {archaon.strength}")
  print(f"Toughness (T): {archaon.toughness}")
  print(f"Agility (Ag): {archaon.agility}")
  print(f"Intelligence (Int): {archaon.intelligence}")
  print(f"Willpower (WP): {archaon.will_power}")
  print(f"Fellowship (Fel): {archaon.fellowship}")
  print(f"Attacks (A): {archaon.attacks}")
  print(f"Maximum health (Wounds - W): {archaon.health_max} and current: {archaon.health}")
  print(f"Strength Bonus (SB): {archaon.strength_bonus} (SB == S // 10)")
  print(f"Toughness Bonus (TB): {archaon.toughness_bonus} (TB == T // 10)")
  print(f"Movement (M): {archaon.movement}")
  print(f"Magic (Mag): {archaon.magic}")  
  print(f"Insanity Points (IP): {archaon.insanity_points}")
  print(f"Fate Points (FP): {archaon.fate_points}")

  print(enemies)
