# Hangman Game 🎯

A classic **Hangman word-guessing game** built with Python. The player attempts to guess a hidden word one letter at a time before running out of attempts.

---

## About the Project

This project demonstrates core Python programming concepts through a fun, interactive terminal game. It is a great example of using loops, conditionals, lists, and basic user input handling to build a complete, working application from scratch.

---

## How It Works

1. The game randomly selects a word from a predefined word list.
2. The player is shown blank spaces representing each letter of the word.
3. The player guesses one letter at a time.
4. A correct guess reveals the letter in its position(s).
5. A wrong guess reduces the number of remaining attempts.
6. The game ends when the player either guesses the full word or exhausts all 6 attempts.

---

## Features

- Random word selection on every game start
- Real-time display of guessed letters and remaining attempts
- Duplicate guess detection to avoid penalizing the player
- Clear win/loss feedback at the end of each game

---

## Tech Stack

| Technology | Purpose              |
|------------|----------------------|
| Python 3.x | Core language        |
| `random`   | Random word selection |

No external libraries or installations required.

---

## Getting Started

**Prerequisites:** Python 3.x installed on your machine.

**Run the game:**

```bash
python hangman.py
```

**Sample gameplay:**

```
Welcome to Hangman Game!
Guess the word one letter at a time.

Word: _ _ _ _ _ _
Guessed letters: []
Remaining attempts: 6
Enter a letter: p

Good guess!
Word: p _ _ _ _ _
Remaining attempts: 6
Enter a letter: z

Wrong guess!
Remaining attempts: 5
```

---

## Project Structure

```
HanGame.py       # Main game file containing all logic
README.md        # Project documentation
```

---

## Concepts Demonstrated

- **Randomization** — using Python's `random` module for dynamic gameplay
- **List manipulation** — tracking guessed letters and building the display
- **Loop control** — managing game state with `while` loops and `continue`
- **String operations** — comparing and revealing characters
- **User input handling** — reading and validating keyboard input

---

## Future Improvements

- Add difficulty levels (easy / medium / hard word lists)
- Integrate an ASCII art hangman drawing that updates with each wrong guess
- Load words dynamically from an external file or API
- Add a scoring system to track wins and losses across sessions

---

## Author
Sania Aftab
