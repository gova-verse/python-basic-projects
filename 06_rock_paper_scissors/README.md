# Rock Paper Scissors (Project 6)

A command-line Rock-Paper-Scissors game with score tracking.

## Run
```bash
python 06_rock_paper_scissors/rps.py
```

## Program Flow (Line-by-Line Explanation)

### `rps.py`
- **Line 1**: File label comment (`rps.py`).
- **Line 2**: Comment listing learning concepts.
- **Line 4**: Imports Python's `random` module.
- **Line 6**: Defines valid choices in a constant list (`rock`, `paper`, `scissors`).
- **Lines 8-9**: `get_computer_choice()` returns one random value from `CHOICES`.
- **Lines 11-19**: `get_winner(player, computer)` compares choices and returns one of:
  - `draw` (same choice),
  - `player` (player-winning combinations),
  - `computer` (all remaining cases).
- **Lines 21-25**: `show_scores(scores)` prints the current player/computer/draw counts.
- **Lines 27-34**: `show_menu()` prints command options (`rock`, `paper`, `scissors`, `score`, `quit`).
- **Lines 36-65**: `play_round(scores)` controls one round:
  - Shows menu and reads input (`line 38`).
  - Handles commands:
    - `quit` → return `False` to stop game (`lines 40-41`).
    - `score` → print scores and continue (`lines 42-44`).
    - invalid choice → show error and continue (`lines 45-47`).
  - Generates computer move (`line 49`) and prints both choices (`lines 50-51`).
  - Computes winner (`line 53`) and updates score dictionary (`lines 55-63`).
  - Returns `True` to continue loop (`line 65`).
- **Lines 67-88**: `main()` function:
  - Prints welcome banner (`lines 68-70`).
  - Initializes score dictionary and rounds variable (`lines 72-73`).
  - Runs loop calling `play_round(scores)` (`lines 75-76`).
  - On quit (`not keep_playing`), calculates total rounds and prints final summary/winner (`lines 78-87`).
  - Breaks loop (`line 88`).
- **Lines 90-91**: Standard entry point; runs `main()` only when file is executed directly.

## Key Data Structures
- `CHOICES` list for valid game moves.
- `scores` dictionary for running totals.

## Suggested Improvements
- Add input aliases (`r`, `p`, `s`).
- Add best-of-N mode.
- Save session scores to file.
