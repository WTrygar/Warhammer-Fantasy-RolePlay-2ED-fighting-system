#imports
from abc import ABC
from random import randint

from health_bar import HealthBar
from warhammer_weapons import fist, hochlandLongRifle

enemies = []
playable_characters = []
all_characters = []

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

    self.main_hand = weapons[0]
    self.off_hand = weapons[0]

    all_characters.append(self)
  
  def __repr__(self):
    return f'{self.name}'
  
  @property
  def alive(self) -> bool:
    return self.health > 0
  
  @staticmethod
  def roll_event_100(stat_chance: int) -> bool:
    rolled_event = randint(1, 100)
    print(f"d100 roll: {rolled_event}")
    return rolled_event > stat_chance
  
  # ----- BASIC ACTIONS -----
  
  def aim(self, target) -> None:
    ... #The character takes extra time to set up a melee or missile attack, thus increasing the chance to hit. If the character's following action is a standard attack, he gains a +10 bonus to weapon_skill (for melee attacks) or ballistic_skill (for ranged attacks).
  
  def cast(self, spell, *targets) -> None:
    ... #the character unleashes a magic spell. If the character spends an extra half action, the casting roll can be augmented with a channelling skill test. Casting can be an extended action. You cannot cast more than one spell per round.

  def charge_attack(self, target) -> None:
    ... #the character rushes up to an opponent and delivers a single attack. The opponent must be at least 2 squares away from the character but within the character's charge move. Last 2 squares of the charge must be in a straight lin, so the charger can build up speed and line up with the target. The charging character gains a 10+ weapon_skill bonus.

  def switch_weapon(self) -> None:
    ... #character can switch a weapon for the other in his weapon list. If not stated, it takes half an action -> time of action == 1

  def use_item(self) -> None:
    ... #character uses an item from it's inventory, takes atleast half an action -> time of action >= 1

  def standard_attack(self, target) -> None:
    if not self.alive:
      print(f"{self.name} has fallen in battle...")
      return
    if self.roll_event_100(self.weapon_skills):
      print(f"{self.name}'s weapon skills: {self.weapon_skills}")
      print(f"{self.name} missed the attack!")
      return
    
    dmg = max(self.main_hand.damage + self.strength_bonus, 1)

    target.get_damaged(dmg, self)
    
  def swift_attack(self, target) -> None:
    ... #The character can make a number of melee or ranged attacks equal to his attacks characteristic. The character must have attacks >= 2 or better to take advantage of this action. If making a missile attack, a character can only use this action if the weapon can be reloaded as a free action or if the chararcter has a loaded pistol weapon in each hand. In the latter case, the character can make a maximum of 2 attacks (one per weapon)

  # ----- ADVANCED ACTIONS -----

  def all_out_attack(self, target) -> None:
    ... #the character makes a furious melee attack, exposing himself to danger in order to land a forceful blow. The character's melee attack gains a 20+ weapon_skill bonus. However, until next turn, the character cannot parry or dodge.

  def defensive_stance(self) -> None:
    ... #the character strikes no blows this round, preferring instead to concentrate on self-defence. Until his next turn all melee attacks against the character suffer a -20 weapon_skill penalty.

  def delay(self) -> None:
    ... #the character waits and watches for an opportunity. When the delay action is used the character's turn ends immediately, but a half action is reserved for later use. Any time before his next turn, the character can take his half action. If two conflicting characters are both trying to use a delayed action simultaneously, make an opposed agility test to see who acts first. If the prepared action is not taken before the character's next turn, it is lost.

  def feint(self, target) -> None:
    ... #the character pretends to attack in one direction, deceiving his opponent and throwing off his defence. This is resolved as an opposed weapon_skill test. If the character wins, his next attack cannot be either dodged or parried. If the character's next action is anything other than a standard attack, this bonus is lost.

  def guarded_attack(self, target) -> None:
    ... #the character attacks carefully, making sure he is well defended from counter blows. He makes a melee attack with a -10 weapon_skill penalty. Until his next turn, the character gains a +10 bonus on any attempted parries and dodges.

  def parrying_stance(self) -> None:
    ... #the character readies to parry an incoming blow. Any time before his next turn, the character can try to parry one successful melee attack agains him as long as he is aware of the attack. Parrying stance ends at the start of his next turn, regardless of whether he parried a blow. Should a character have a weapon in their left hand. (this included shields and bucklers) he may parry once per round as a free action.
    
    
  # ----- HELPER FUNCTIONS ----- 
  def get_damaged(self, dmg: int, attacker) -> None:
    self.health -= dmg
    self.health = max(self.health, 0)
    self.health_bar.update()
    print(f"{attacker.name}'s weapon skills: {attacker.weapon_skills}")
    print(f"{attacker.name} dealt {dmg} damage to {self.name} with {attacker.main_hand.name}")

# ----- First Child Class -----
class PlayerCharacter(Character):
  def __init__(self, name, race, career, weapon_skill, ballistic_skill, strength, toughness, agility, intelligence, will_power, fellowship, attacks, health_max, health, movement, magic, insanity_points, fate_points, weapons, items, spells) -> None:
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

    self.health_bar = HealthBar(self, color="green")

    playable_characters.append(self)

# -----Second Child Class-----
class EnemyCharacter(Character):
  def __init__(self, name, race, career, weapon_skill, ballistic_skill, strength, toughness, agility, intelligence, will_power, fellowship, attacks, health_max, health, movement, magic, insanity_points, fate_points, weapons, items, spells) -> None:
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

    self.health_bar = HealthBar(self, color="red")

    enemies.append(self)