# 🍕 Pizza Survivor

**Pizza Survivor** is a 2D survival game developed with **Python and Pygame**. The player controls a pizza delivery character who must survive waves of enemies while automatically shooting pizzas at the nearest target.

As time passes, the difficulty increases and enemies appear more frequently, making survival progressively more challenging.

## 🎮 Features

* 🕹️ Player movement using the keyboard.
* 🐶 Dogs and 🐱 cats as different enemy types.
* 🎯 Enemies automatically follow the player.
* 🍕 Automatic pizza shooting toward the nearest enemy.
* ❤️ Life system with temporary invulnerability after receiving damage.
* 💥 Collision detection between the player, enemies, and pizzas.
* 🏆 Score system based on defeated enemies.
* ⏱️ Game timer.
* 📈 Progressive difficulty system:

  * Enemies initially spawn every 3 seconds.
  * Spawn frequency increases as time passes.
  * The minimum spawn interval is 0.5 seconds.
* 🎁 Life power-up:

  * A pizza box appears randomly every 15–20 seconds.
  * Collecting it restores one life.
  * The player can have a maximum of 5 lives.
  * The power-up disappears automatically after 5 seconds.
* 🎵 Background music and sound effects.
* 💀 Game Over screen displaying the final score and survival time.

## 🛠️ Technologies

* Python
* Pygame
* Object-Oriented Programming (OOP)
* Git
* GitHub

## 🧩 Project Structure

The project follows an object-oriented approach, separating the responsibilities of the different game components into individual modules.

```text
pizza_survivor/
│
├── main.py
├── enemy.py
├── dog.py
├── cat.py
├── dealer.py
├── pizza.py
├── pizza_box.py
├── interface.py
│
└── assets/
    └── images and sounds
```

> The exact asset organization may vary depending on the current version of the project.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/julianaflorezm/pizza_survivor.git
```

### 2. Enter the project directory

```bash
cd pizza_survivor
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python main.py
```

## 🎯 Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬅️ Left Arrow  | Move left  |
| ➡️ Right Arrow | Move right |
| ⬆️ Up Arrow    | Move up    |
| ⬇️ Down Arrow  | Move down  |

Pizza shooting is automatic and targets the nearest enemy.

## 🧠 What I Practiced

This project allowed me to reinforce concepts such as:

* Object-Oriented Programming in Python.
* Classes and inheritance.
* Game loops.
* Event handling with Pygame.
* Collision detection.
* Working with timers.
* Random enemy generation.
* Managing game states.
* Progressive difficulty.
* Separation of responsibilities between modules.
* Working with images, music, and sound effects.

## 🔮 Possible Improvements

Some features that could be added in future versions:

* Different types of power-ups.
* Multiple difficulty levels.
* Start and restart menus.
* High-score persistence.
* Additional enemy types.
* Different weapons or pizza attacks.
* Boss enemies.
* Improved animations.

## 👩‍💻 Author

**Juliana Florez**

Developed as part of my Python learning journey, applying programming fundamentals, Object-Oriented Programming, and game development concepts with Pygame.
