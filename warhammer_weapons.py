meele_weapons: list = []
missile_weapons: list = []

class Weapon:
  def __init__(self,
               name: str,
               cost: int,
               encumbrance: int,
               group: str,
               damage: int,
               qualities: list,
               availability: str):
    self.name = name
    self.cost = cost
    self.encumbrance = encumbrance
    self.group = group
    self.damage = damage
    self.qualities = qualities
    self.availability = availability
    
  def __repr__(self):
    return f'{self.name}'

class MeleeWeapon(Weapon):
  def __init__(self, name, cost, encumbrance, group, damage, qualities, availability):
    super().__init__(name, cost, encumbrance, group, damage, qualities, availability)

    meele_weapons.append(self)


class MissileWeapon(Weapon):
  def __init__(self, name, cost, encumbrance, group, damage, qualities, availability, range: list, reload: int):
    super().__init__(name, cost, encumbrance, group, damage, qualities, availability)
    self.range = range
    self.reload = reload

    missile_weapons.append(self)


fists = MeleeWeapon(name = "Fists",
                    cost = 0,
                    encumbrance = 0,
                    group = "Ordinary",
                    damage = 1,
                    qualities = [],
                    availability = "Common")

hochlandLongRifle = MissileWeapon(name = "Hohland Long Rifle",
                               cost = 450,
                               encumbrance = 70,
                               group = "Engineer",
                               damage = 4,
                               range = [48, 96],
                               reload = 4,
                               qualities = ["Impact", "Unreliable"],
                               availability = "Very Rare")

#TESTING
if __name__ == "__main__":
  print(f"Weapon name: {fists.name}")
  print(f"Cost: {fists.cost}")
  print(f"Encumbrance: {fists.encumbrance}")
  print(f"Group: {fists.group}")
  print(f"Damage: {fists.damage}")
  print(f"Qualities: {fists.qualities}")
  print(f"Availability: {fists.availability}")
  print(f" ")
  print(f"Weapon name: {hochlandLongRifle.name}")
  print(f"Cost: {hochlandLongRifle.cost}")
  print(f"Encumbrance: {hochlandLongRifle.encumbrance}")
  print(f"Group: {hochlandLongRifle.group}")
  print(f"Damage: {hochlandLongRifle.damage}")
  print(f"Range: {hochlandLongRifle.range}")
  print(f"Reload: {hochlandLongRifle.reload}")
  print(f"Qualities: {hochlandLongRifle.qualities}")
  print(f"Availability: {hochlandLongRifle.availability}")
  print(f" ")
  print(meele_weapons)
  print(missile_weapons)