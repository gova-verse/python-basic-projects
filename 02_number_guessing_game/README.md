# Number Guessing Game (Python)

A Python CLI game where the system picks a number and the user tries to guess it within limited attempts.

## Features
- Random secret number
- High/low hints after each guess
- Input validation (`try/except`)
- Attempt counter with max attempts
- Replay option

## How to Run
From the repository root:

```bash
python 02_number_guessing_game/guessing_game.py
```

## Code Walkthrough (Line-by-Line)
> File: `02_number_guessing_game/guessing_game.py`

### 1) Imports and helper functions
- **Line 3**: Imports `random` module.
- **Lines 4-6**: `get_random_number(min_val, max_val)` returns random integer.
- **Lines 7-14**: `check_guess(guess, secret)` returns `too low`, `too high`, or `correct`.

### 2) Game setup
- **Lines 15-18**: Prints game banner.
- **Lines 20-24**: Sets range, generates secret number, initializes attempts.
- **Lines 26-27**: Shows instructions to the player.

### 3) Guess loop
- **Line 29**: Runs loop while attempts are available.
- **Lines 31-32**: Displays remaining attempts.
- **Lines 35-39**: Validates integer input with `try/except`.
- **Lines 41-43**: Validates range (`1` to `100`).
- **Lines 44-45**: Counts attempt and checks guess result.

### 4) Win/lose conditions
- **Lines 47-55**: If correct, prints success message and returns `True`.
- **Lines 56-57**: If wrong, prints hint.
- **Lines 60-62**: After attempts end, prints game-over + secret number.

### 5) Replay loop (program entry)
- **Lines 63-69**: `main()` allows replay until user types anything other than `yes`.
- **Lines 70-71**: Runs `main()` when file is executed directly.

## Example
```text
I picked a number between 1 and 100.
You have 7 attempts.
Attempts remaining: 7
Enter your guess: 50
Your guess is too low
```

## Optional Next Improvements
- Difficulty levels (easy/medium/hard)
- Scoreboard based on attempts
- Save best score to a file
