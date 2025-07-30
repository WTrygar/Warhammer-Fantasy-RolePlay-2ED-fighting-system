#here will be a list of spells (functions or objects) that characters with Magic > 0 could use
from abc import ABC


class Spell(ABC):
  def __init__(self, name: str, casting_number: int, ingridient: object, ingridient_bonus: int, description: str):
    self.name = name
    self.casting_number = casting_number
    self.ingridient = ingridient
    self.ingridient_bonus = ingridient_bonus
    self.description = description

class DamagingSpell(Spell):
  def __init__(self, name, casting_number, ingridient, ingridient_bonus, description, damage: int, multi_target: bool):
    super().__init__(name = name, casting_number = casting_number, ingridient = ingridient, ingridient_bonus = ingridient_bonus, description = description)

    self.damage = damage
    self.multi_target = multi_target

fires_of_uzhul: DamagingSpell = DamagingSpell(name = "Fires of U'Zhul",
                              casting_number = 6,
                              ingridient = match,
                              damage = 6,
                              multi_target = False
                              description = "You can throw a bolt of fire at an opponent within 36 yards (18 squares) of You. this is a magic missile with Damage 4.")
