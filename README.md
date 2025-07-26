# Warhammer Fantasy Roleplay 2nd Edition Battle Tracker

WFRP 2ED has a lot of data to follow for game masters, especially during combat.
That's why I'm making an app that keeps track of the battle for the game master.

## What can it do?

Once the user runs the code, menu shows up:

- battle,
- create character (the process is implemented but doesn't save the character anywhere),
- update character (not yet implemented),
- rearrange teams,

### Battle

Right now code can handle group battles that ends when all of the heroes or all of the enemies are dead.
Characters can either attack anyone, or do nothing (more actions will be added in the future).
Each character has 4 action points while each action costs are different:

- attack: 2 points,
- do nothing: all points remaining (skip to the next character).

### Rearrange Teams

User can picks either Heroes or Enemies and edit which characters should participate in the battle.

## List of ideas for future updates

Features that will be added in the future:

- new character creation,
- updating the character,
- casting spells -> create a spell class,
- using items -> create an item class,
- more actions -> create functions in Character class,
- characters that value of attribute "attacks" is atleast 2, should be able to perform multiple attacks. If "attacks" is set to 1, it should be forbidden.
- create more characters and weapons.

## Project setup

To run this app, download the code and install inquirer:

```
pip install inquirer
```

after that, open main.py and run it, battle will start!
