# 🎲 Chō-Han Game (丁半)

A graphical implementation of the traditional Japanese **Chō-Han (丁半)** dice game, developed in Python using **Tkinter** and **Pillow**.

The game allows a player to choose between **Chō (丁)** and **Han (半)**, rolls two dice, and determines the winner based on whether the total is even or odd.

---

## 📌 About the Game

Chō-Han is a traditional Japanese dice game in which two dice are rolled and the resulting sum determines whether the outcome is:

- **Chō (丁)** → Even number
- **Han (半)** → Odd number

In this implementation:

1. The player selects **Chō** or **Han**.
2. The computer randomly selects its choice.
3. Two dice are rolled.
4. The dice sum is calculated.
5. The winner is determined.
6. The player and computer scores are updated.
7. The game continues for the selected number of rounds.
8. At the end of the game, the final winner is displayed.

---

## ✨ Features

- 🎲 Random two-dice rolling
- 🧑 Player vs. 🤖 Computer gameplay
- ⚖️ Chō/Han even-odd game logic
- 🔢 User-defined number of rounds
- 🏆 Round-by-round score tracking
- 📊 Player and computer scores displayed during gameplay
- 🎯 Player and computer choices displayed after each round
- 🈳 Japanese Chō-Han terminology
- 🖼️ Custom background and character images
- 🖥️ Maximized graphical interface
- 📐 Responsive background and character image resizing
- 🔄 Play Again functionality
- 🚪 Exit button on the final winner screen
- 🧹 Automatic cleanup of previous round widgets to prevent overlapping UI elements

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| Pillow | Image loading, resizing and cropping |
| Random | Dice rolls and computer choices |
| pathlib | Cross-platform asset path handling |

---

## 📁 Project Structure

```text
Cho-han/
│
├── assets/
│   ├── background.png
│   ├── bot.png
│   └── player.png
│
├── src/
│   └── cho_han_game.py
│
├── requirements.txt
└── README.md
