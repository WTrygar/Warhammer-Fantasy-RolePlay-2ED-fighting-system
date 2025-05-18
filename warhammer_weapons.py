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
               availability: str,
               two_handed: bool):
    self.name = name
    self.cost = cost
    self.encumbrance = encumbrance
    self.group = group
    self.damage = damage
    self.qualities = qualities
    self.availability = availability
    self.two_handed = two_handed
    
  def __repr__(self):
    return f'{self.name}'

class MeleeWeapon(Weapon):
  def __init__(self, name, cost, encumbrance, group, damage, qualities, availability, two_handed):
    super().__init__(name, cost, encumbrance, group, damage, qualities, availability, two_handed)

    meele_weapons.append(self)


class MissileWeapon(Weapon):
  def __init__(self, name, cost, encumbrance, group, damage, qualities, availability, two_handed, range: list, reload: int):
    super().__init__(name, cost, encumbrance, group, damage, qualities, availability, two_handed)
    self.range = range
    self.reload = reload

    missile_weapons.append(self)

# ----- ONE HANDED MELEE WEAPONS -----
fist = MeleeWeapon(name = "Fist",
                    cost = 0,
                    encumbrance = 0,
                    group = "Ordinary",
                    damage = -4,
                    qualities = [],
                    availability = "Common",
                    two_handed = False)

axe = MeleeWeapon(name = "Axe",
                        cost = 60,
                        encumbrance = 45,
                        group = "Ordinary",
                        damage = 0,
                        qualities = ["Impact"],
                        availability = "Scarce",
                        two_handed = False)

hammer = MeleeWeapon(name = "Hammer",
                        cost = 70,
                        encumbrance = 65,
                        group = "Ordinary",
                        damage = 0,
                        qualities = ["Pummelling"],
                        availability = "Scarce",
                        two_handed = False)

militaryPick = MeleeWeapon(name = "Military Pick",
                        cost = 90,
                        encumbrance = 60,
                        group = "Ordinary",
                        damage = 0,
                        qualities = ["Armour Piercing", "Slow"],
                        availability = "Very Rare",
                        two_handed = False)

sword = MeleeWeapon(name = "Sword",
                        cost = 45,
                        encumbrance = 45,
                        group = "Ordinary",
                        damage = 0,
                        qualities = ["Defensive"],
                        availability = "Scarce",
                        two_handed = False)

# ----- TWO HANDED MELEE WEAPONS -----
greatAxe = MeleeWeapon(name = "Great Axe",
                        cost = 120,
                        encumbrance = 180,
                        group = "Two-handed",
                        damage = 1,
                        qualities = ["Impact", "Slow", "Tiring"],
                        availability = "Rare",
                        two_handed = True)

# ----- MISSILE WEAPONS -----
hochlandLongRifle = MissileWeapon(name = "Hohland Long Rifle",
                               cost = 450,
                               encumbrance = 70,
                               group = "Engineer",
                               damage = 4,
                               range = [48, 96],
                               reload = 4,
                               qualities = ["Impact", "Unreliable"],
                               availability = "Very Rare",
                               two_handed = True)

# ----- TESTING -----
if __name__ == "__main__":
  print(f"Weapon name: {fist.name}")
  print(f"Cost: {fist.cost}")
  print(f"Encumbrance: {fist.encumbrance}")
  print(f"Group: {fist.group}")
  print(f"Damage: {fist.damage}")
  print(f"Qualities: {fist.qualities}")
  print(f"Availability: {fist.availability}")
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