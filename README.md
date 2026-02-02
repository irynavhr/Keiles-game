# Keiles Game

Keiles Game is a classic logical matchstick game implemented in two versions:

- Python (pygame) — graphical version  
- Go (Golang) — console version  

The project can be used both for playing the game and as an educational example of simple game logic implemented in different programming languages.

---

## Game Description

At the start of the game, there is a fixed number of matchsticks.  
Players take turns making moves.

On each turn, a player may:
- remove 1 matchstick
- remove 2 matchsticks

The player who removes the last matchstick loses.  
The objective of the game is to force the opponent to make the final move.

The game demonstrates:
- logical thinking
- use of conditions and loops
- basic game strategy principles
- implementation of the same algorithm in multiple programming languages

---

## Project Structure

```

Keiles_game/
│
├── Keiles_game_golang_version/
│   └── Keiles_game.go
│
├── Keiles_game_python_version/
│   ├── Keiles_game.py
│   ├── game-icon.png
│   ├── match.png
│   ├── burning-match.png
│   └── burned-match.png

````

---

## Python Version (pygame)

### Requirements
- Python 3.8 or newer
- pygame

### Installation
```bash
pip install pygame
````

### Run

```bash
python Keiles_game.py
```

### Features

* graphical user interface
* matchstick visualization
* event handling using pygame
* simple and readable game logic

---

## Go Version (Golang)

### Requirements

* Go 1.18 or newer

### Run

```bash
go run Keiles_game.go
```

### Features

* console-based implementation
* clear and minimal logic
* suitable for educational and demonstration purposes

---

## Technologies

* Python (pygame)
* Go (Golang)

---

## Author

Iryna Hrytsenko

---

## License

This project is intended for educational purposes.
You are free to use, modify, and distribute this code.

