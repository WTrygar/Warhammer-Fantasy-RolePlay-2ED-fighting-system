# here will be a list of items that characters can have in their inventory that are not weapons
from abc import ABC


class Item(ABC):
  def __init__(self, name: str, cost: int, encumbrance: int, availability: str, description: str):
    self.name = name
    self.cost = cost
    self.encumbrance = encumbrance
    self.availability = availability
    self.description = description

class LighingItem(Item):
  def __init__(self, name, cost, encumbrance, availability, description):
    super().__init__(name, cost, encumbrance, availability, description)

match: LighingItem = LighingItem(name = "Match",
                                 cost = 1,
                                 encumbrance = 0,
                                 availability = "Avarage",
                                 description = "A match is a thin sliver of wood with one end chemically treated to produce a flame when drawn across a rough surface. Any given match has a 50 percent chance of lighting. A poorly constructed match reduces this chance to 25 percent, while a goodly crafted match ignites 75 percent of the time, and those of best craftsmanship always light.")