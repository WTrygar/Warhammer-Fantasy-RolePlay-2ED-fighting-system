def check_index() -> None: #function that keeps track of which character turn it is, skips those that are dead
  while characters_static[Game.index].health == 0: #check if current character is dead
    print(f"CHARACTER IS DEAD current value of index: {Game.index} - {characters_static[Game.index]}")
    if Game.index + 1 != len(characters_static):
      Game.index += 1
      print(f"CHARACTER: {characters_static[Game.index]} - {Game.index}")
    elif Game.index + 1 >= len(characters_static):
      Game.index = 0
      print(f"Out of bounds, lets reset back to zero : {Game.index}")
    else:
      Game.index += 1
      print(f"DEAD not zero increment: {Game.index}")
    print(characters_static[Game.index])
  if Game.index + 1 >= len(characters_static):
    Game.index = 0
    while characters_static[Game.index].health == 0:
      print(f"DEAD current value of index: {Game.index}")
      if Game.index == 0:
        Game.index += 1
        print(f"DEAD index was 0, hence increment: {Game.index}")
      elif Game.index + 1 >= len(all_characters):
        Game.index = 0
        print(f"DEAD index would get out of range, so we set it to 0: {Game.index}")
      else:
        Game.index += 1
        print(f"DEAD not zero increment: {Game.index}")
      print(characters_static[Game.index])
    print(f"NOT DEAD out of bounds: {Game.index}")
  elif characters_static[Game.index].health != 0:
    print(f"now was {characters_static[Game.index]}'s turn - index: {Game.index}")
    Game.index += 1
    print(f"NOT DEAD increment: now will be {characters_static[Game.index]}'s turn - index: {Game.index}")
  return