# Sopwith Python

A nostalgic remake of the classic Sopwith game, originally enjoyed on the Commodore Vic 20. This Python version recreates the simple yet addictive gameplay of piloting a biplane and bombing targets on the ground.

## About

This project is a personal learning journey into Python game programming using Pygame. It's a fun tribute to a childhood favorite, where you control a Sopwith biplane and attempt to clear all buildings and objects from the ground so your plane can safely land.

## Game Objective

- Pilot your Sopwith biplane across the terrain
- Drop bombs to destroy all buildings and objects on the ground
- Clear the area to allow your plane to land safely
- Use as few bombs as possible to achieve a better score

## Features

- Classic side-scrolling airplane gameplay
- Simple, intuitive controls
- Bomb dropping mechanics
- Score tracking (number of bombs used)
- Retro-style graphics inspired by the original

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/sopwith_python.git
cd sopwith_python
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install pygame
```

## How to Run

```bash
python src/sopwith.py
```

## Controls

- **SPACE** - Drop bomb
- **ESC** or close window - Quit game

## Project Structure

```
sopwith_python/
├── src/
│   ├── sopwith.py          # Main game script
│   └── assets/
│       └── images/
│           ├── sopwith.png    # Airplane sprite
│           ├── bomb.png       # Bomb sprite
│           └── background.png # Game background
├── .gitignore
└── README.md
```

## Development

This project is open source and available on GitHub for anyone to fork, modify, and learn from. Feel free to contribute improvements, add features, or use it as a learning resource for Python game development.

### Future Enhancements (Ideas)

- Add destructible buildings and targets
- Implement collision detection
- Add sound effects and music
- Create multiple levels with increasing difficulty
- Add enemy planes or anti-aircraft guns
- Implement a landing mechanism
- High score tracking
- Multiple lives system

## Learning Goals

- Practice Python programming
- Learn Pygame library and game development concepts
- Understand game loops, sprites, and collision detection
- Have fun recreating a childhood memory!

## License

This is an open-source learning project. Feel free to use, modify, and distribute as you see fit.

## Acknowledgments

- Original Sopwith game creators for the inspiration
- The Pygame community for excellent documentation and resources
- Commodore Vic 20 for providing countless hours of childhood entertainment

---

**Note:** This is a work in progress and a learning project. Contributions and suggestions are welcome!