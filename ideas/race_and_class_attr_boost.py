#  IDEAS FOR RACES AND CAREERS ADDING BONUS STATS AND DATA TO CHARACTERS
from random import randint
bonus_stat_dict = {
  "elf": {
    "weapon_skill": 20,
    "ballistic_skill": 30,
    "strength": 20,
    "toughness": 20,
    "agility": 30,
    "intelligence": 20,
    "will_power": 20,
    "fellowship": 20,
    "movement": 5,
    "fate_points": randint(1, 2),
    "skills": ["common_knowledge_elves", "speak_language_eltharin", "speak_language_reikspiel"],
    "talents": ["aethyric_attunement" or "specialist_weapon_group_longbow", "coolheaded" or "savvy", "excellent_vision", "night_vision"]
  },
  "kithband warrior": {
    "weapon_skill": 5,
    "ballistic_skill": 5,
    "agility": 10,
    "intelligence": 10,
    "will_power": 5,
    "max_health": 2,
    "skills": ["concealment", "dodge_blow", "follow_trail", "heal" or "search", "outdoor_survival", "perception", "scale_sheer_surface", "silent_move"],
    "talents": ["marksman" or "rover", "rapid_reload" or "warrior_born"],
    "weapons": ["elf_bow", {"arrows": 10}],
    "armor": ["leather_jacket"],
    "items": []
  }
}
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