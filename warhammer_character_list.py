from warhammer_character import (EnemyCharacter, PlayerCharacter,
                                 all_characters, enemies, playable_characters)
from warhammer_weapons import axe, fist, hochlandLongRifle

# ----- PLAYABLE CHARACTERS -----
helmut: PlayerCharacter = PlayerCharacter(name = "Helmut",
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
                         weapons = [fist, hochlandLongRifle],
                         items = [],
                         spells = ())

# snorri: PlayerCharacter = PlayerCharacter(name = "Snorri",
#                          race = "Dwarf",
#                          career = "Slayer",
#                          weapon_skill = 35,
#                          ballistic_skill = 25,
#                          strength = 35,
#                          toughness = 35,
#                          agility = 30,
#                          intelligence = 20,
#                          will_power = 30,
#                          fellowship = 25,
#                          attacks = 1,
#                          health_max = 15,
#                          health = 15,
#                          movement = 3,
#                          magic = 0,
#                          insanity_points = 0,
#                          fate_points = 2,
#                          weapons = [fist, axe],
#                          items = [],
#                          spells = ())

# lerthan: PlayerCharacter = PlayerCharacter(name = "Lerthan",
#                          race = "Elf",
#                          career = "kithband warrior",
#                          weapon_skill = 30,
#                          ballistic_skill = 35,
#                          strength = 30,
#                          toughness = 30,
#                          agility = 40,
#                          intelligence = 25,
#                          will_power = 30,
#                          fellowship = 35,
#                          attacks = 1,
#                          health_max = 13,
#                          health = 13,
#                          movement = 5,
#                          magic = 0,
#                          insanity_points = 0,
#                          fate_points = 1,
#                          weapons = [fist, hochlandLongRifle ],
#                          items = [],
#                          spells = ())



# ----- ENEMY CHARACTERS -----
archaon: EnemyCharacter = EnemyCharacter(name = "Archaon the Everchosen",
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
                         weapons = [fist],
                         items = [],
                         spells = ())

# manfred: EnemyCharacter = EnemyCharacter(name = "Manfred",
#                          race = "Vampire",
#                          career = "Vampire Lord",
#                          weapon_skill = 60,
#                          ballistic_skill = 40,
#                          strength = 60,
#                          toughness = 60,
#                          agility = 50,
#                          intelligence = 70,
#                          will_power = 70,
#                          fellowship = 50,
#                          attacks = 2,
#                          health_max = 50,
#                          health = 50,
#                          movement = 4,
#                          magic = 3,
#                          insanity_points = 10,
#                          fate_points = 3,
#                          weapons = [fist],
#                          items = [],
#                          spells = ())


# ----- TESTING -----
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
  print(f"Weapons: {helmut.weapons}")
  print(f"What's in main hand?: {helmut.main_hand}")
  print(f"What's in off hand?: {helmut.off_hand}")

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
  print(f" ")
  print(f"List of all characters: {all_characters}")
  print(f"List of enemies: {enemies}")
  print(f"List of playable characters: {playable_characters}")
  
