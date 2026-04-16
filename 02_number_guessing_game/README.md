# Number Guessing Game (Python)

A beginner-friendly command-line number guessing game built in Python.

## Features
- Random secret number generation using `random.randint()`
- User-friendly hints after each guess:
  - `too low`
  - `too high`
  - `correct`
- Input validation for non-numeric and out-of-range guesses
- Limited attempts to make gameplay more fun
- Option to replay after each round

## Project Goal
This project helps beginners practice:
- `while` loops and game flow control
- Conditional logic (`if`/`elif`/`else`)
- Functions and return values
- Exception handling with `try`/`except`
- Basic use of Python's `random` module

## File Structure
```text
02_number_guessing_game/
├── guessing_game.py
└── README.md
```

## How to Run
From the repository root:

```bash
python 02_number_guessing_game/guessing_game.py
```

## Example
```text
I picked a number between 1 and 100.
You have 7 attempts. Good luck

Attempts remaining: 7
Enter your guess: 50
Your guess is too low:
```

## Notes
- The game currently uses a range of `1` to `100` and allows `7` attempts.
- You can extend it with difficulty levels, score tracking, or hints based on distance.
