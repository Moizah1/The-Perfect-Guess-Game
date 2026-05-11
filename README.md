# 🎯 The Perfect Guess

A number guessing game built with Python, available in both a **command-line** and a **graphical (GUI)** version. The program generates a random number between 1 and 100, and the player must guess it — with hints given after each attempt.

---

## 📁 Project Structure

```
the-perfect-guess/
├── main.py       # Command-line version
├── gui.py        # GUI version using Tkinter
└── README.md
```

---

## 🚀 Features

- Random number generation between 1 and 100
- "Higher" / "Lower" hints after each guess
- Tracks the number of attempts
- GUI version includes a reset button to start a new game
- Input validation to handle non-numeric entries (GUI)

---

## 🖥️ How to Run

### Command-Line Version

```bash
python main.py
```

**Example interaction:**

```
Guess the number: 50
Higher number please
Guess the number: 75
Lower number please
Guess the number: 63
You have guessed the number 63 correctly in 3 attempts
```

---

### GUI Version

```bash
python gui.py
```

The GUI window will open. Type your guess in the input field and click **Submit Guess**. Use the **Reset Game** button to start over at any time.

> **Requirement:** Tkinter is included with standard Python installations. No additional packages needed.

---

## 🛠️ Requirements

- Python 3.x
- Tkinter *(included in standard Python — no extra install needed)*

---

## 📦 Installation

```bash
# Clone the repository
git clone (repository)

# Navigate into the project folder
cd the-perfect-guess

# Run either version
python main.py      # CLI
python gui.py       # GUI
```

---

## 🧠 How It Works

1. A random integer between **1 and 100** is generated at the start.
2. The player enters a guess.
3. The program responds with:
   - **"Higher number please"** — if the guess is too low
   - **"Lower number please"** — if the guess is too high
   - **Congratulations message** — when the correct number is guessed, along with the attempt count.
4. In the GUI version, the game resets automatically after a correct guess.

