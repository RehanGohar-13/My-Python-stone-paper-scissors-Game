# Stone Paper Scissors — Roguelike Edition
### By Iwen (RehanGohar-13)

> *"The oldest game in the world. Reimagined."*

---

## What is this?

This is not your average Stone Paper Scissors game.

It started as a simple terminal script and evolved into 
a fully featured desktop game with a custom dark UI, 
difficulty levels, and a roguelike progression system 
inspired by games like Balatro and Gambonanza.

Built entirely in Python using CustomTkinter.
No game engine. No shortcuts. Just pure code.

---

## Current Version: 1.0 (Base Game)

### Features:
| Feature | Status |
|---------|--------|
| Stone Paper Scissors core logic | ✅ |
| Dark Maroon/Crimson UI | ✅ |
| First to 3 wins system | ✅ |
| Score tracking | ✅ |
| Round counter | ✅ |
| Game over screen | ✅ |
| Play Again button | ✅ |
| CPU opponent | ✅ |

---

## Roadmap: Version 2.0 (Roguelike Edition)

This is where it gets interesting.

### Difficulty Levels:
| Mode | How CPU behaves |
|------|----------------|
| **Easy** | CPU makes bad decisions on purpose |
| **Normal** | Pure random (classic) |
| **Hard** | CPU learns your patterns |
| **Impossible** | CPU always counters you (easter egg) |

### Stage System:
Stage 1: Easy CPU
Win 3 rounds → Pick a Power Up → Advance
↓
Stage 2: Normal CPU
Win 3 rounds → Pick a Power Up → Advance
↓
Stage 3: Hard CPU (learns patterns)
Win 4 rounds → Pick a Power Up → Advance
↓
Stage 4: Boss Battle
↓
Stage 5: The Void (Final Boss)


### Power Ups:
| Power Up | Effect |
|----------|--------|
| **Double Strike** | Win counts as 2 points |
| **Shield** | First loss doesn't count |
| **Mind Read** | See CPU choice once per game |
| **Lucky Coin** | Ties count as wins |
| **Time Bomb** | Win 3 in a row = instant stage clear |
| **Mirror** | CPU copies your last move |
| **Poison** | Every tie damages CPU |
| **Gambler** | Double or nothing each round |
| **Cursed Hand** | One of your options removed |
| **Weighted Dice** | Rock beats paper 30% of time |

### Boss Battles:
| Boss | Special Ability |
|------|----------------|
| **The Mirror** | Always copies your previous move |
| **The Prophet** | 50% chance of seeing your move |
| **The Gambler** | Random crazy effects each round |
| **The Void** | Has all power ups you rejected |
| **The Final Hand** | Cheats but you have everything |

### Roguelike Features:
- **Permadeath:** Lose = start from Stage 1
- **Run History:** Track your best runs
- **High Score:** How far can you get?
- **Power Up choices:** Pick 1 of 3 after each stage

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| UI Framework | CustomTkinter |
| Game Logic | Pure Python |
| Color Scheme | Maroon, Crimson, Dark Red |

---

## How to Run

```bash
# Install dependency
pip install customtkinter

# Run the game
python rps_game.py
```

---

## The Story Behind It

This game started as a simple terminal script:

```bash
player_choice = input("Enter a choice (rock, paper, scissors): ")
```

One line. No UI. No score. No logic beyond win/lose.

It became a proper desktop game with a dark theme,
animations, and a full roguelike progression system
planned — all because the developer refused to stop
at "good enough."

---

## Why Roguelike?

Every run is different.
Every power up changes your strategy.
Every boss requires a new approach.

Stone Paper Scissors has been played for thousands of
years. Nobody has ever made it a roguelike before.

Until now.

---

## License

Copyright (c) 2026 Iwen

Creative Commons Attribution-NonCommercial 4.0

You are free to:
- View and study this code
- Share it with attribution

You may NOT:
- Use it commercially
- Sell it or any derivative
- Claim it as your own work

Original concept and implementation by Iwen.
Built in Pakistan.

---

## Author

Iwen

Built in Pakistan. Original idea. Nobody has done this before.

---

## Status

Version 1.0 — Base Game Complete
Version 2.0 — Roguelike Edition (In Development)
The oldest game in the world is about to get a lot more interesting.

---

## What to do with this:

1. Create a new GitHub repo called `stone-paper-scissors-roguelike`
2. Add your `rps_game.py` file
3. Add this as `README.md`
4. Push it to GitHub

**This establishes YOU as the original creator with a timestamp on GitHub. Nobody can claim this idea after today.**

Good luck moving the PC! See you when you are back. 🎮
