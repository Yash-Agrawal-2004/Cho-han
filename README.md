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
```
---

## ⚙️ Requirements

- Python 3.10 or newer
- Pillow
- Tkinter

> **Note:** Tkinter is included with standard Python installations on Windows.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Yash-Agrawal-2004/Cho-han.git
```

### 2. Navigate to the Project Directory

```bash
cd Cho-han
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Command Prompt:**

```bash
venv\Scripts\activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Game

From the project root directory:

```bash
python src/cho_han_game.py
```

The game will open in a maximized graphical window.

---

## 🎮 How to Play

### Step 1 — Start the Game

Click the **Start** button to begin.

### Step 2 — Select Number of Rounds

Enter the number of rounds you want to play and click **Begin**.

### Step 3 — Make Your Choice

For every round, choose:

- **cho** → Chō (Even)
- **han** → Han (Odd)

Then click **Next**.

### Step 4 — Round Result

The game will:

1. Generate the computer's choice.
2. Roll two dice.
3. Calculate the dice total.
4. Determine the round winner.
5. Update the scores.
6. Display the player and computer choices.
7. Display the dice result.

### Step 5 — Continue Playing

If more rounds remain, the next round starts automatically.

The current scores and round information are updated for each round.

### Step 6 — Game Over

After the final round, the **GAME OVER** screen is displayed.

Click **Winner** to view the final result.

### Step 7 — Final Winner Screen

The winner screen displays the winning character and provides:

- **Play again** — Start another game.
- **Exit** — Close the game.

---

## 🧠 Game Logic

The game rolls two six-sided dice:

```text
Dice 1 + Dice 2 = Total
```

The total determines whether the result is **Chō** or **Han**.

### Chō (丁)

An even dice total:

```text
2, 4, 6, 8, 10, 12
```

### Han (半)

An odd dice total:

```text
3, 5, 7, 9, 11
```

The player's and computer's selected choices are compared with the dice result to determine the winner of each round.

---

## 🏆 Scoring

The score is updated after every round.

- **Player wins** → Player score increases by 1
- **Computer wins** → Computer score increases by 1
- **Tie** → Both scores increase by 1

The current scores remain visible throughout the game.

---

## 🖥️ User Interface

The game interface is built using **Tkinter** and includes:

- Game title
- Player score
- Computer score
- Player character
- Computer character
- Round information
- Choice selection
- Round result
- Next button
- Game Over screen
- Winner screen
- Play Again button
- Exit button

The interface is designed to work with different window sizes. Background and character images are dynamically resized to maintain the layout.

---

## 🔄 Play Again

After the game ends, clicking **Play again** returns to the round-selection screen.

The previous game's widgets and results are cleared before the new game begins.

---

## 📸 Screenshots

Screenshots of the game can be added here.

Example:

```text
Add screenshots of:
- Main screen
- Round screen
- Game Over screen
- Winner screen
```

---

## 🔮 Future Improvements

Possible future enhancements include:

- 🎵 Sound effects
- 🎲 Animated dice
- 🏅 High-score system
- 📊 Game statistics
- 🌓 Theme customization
- 🏆 Leaderboard
- 🎚️ Difficulty levels
- 📦 Windows executable release

---

## 👨‍💻 Author

**Yash Agrawal**

GitHub:  
https://github.com/Yash-Agrawal-2004

---

## 📄 License

This project is available for educational and personal use.
