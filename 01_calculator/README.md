# Calculator (Python)

A beginner-friendly command-line calculator built in Python.

## Features
- Basic arithmetic operations: add, subtract, multiply, divide
- Input handling from terminal
- Loop to run multiple calculations
- Divide-by-zero safety check

## How to Run
From the repository root:

```bash
python 01_calculator/calculator.py
```

## Code Walkthrough (Line-by-Line)
> File: `01_calculator/calculator.py`

### 1) Function definitions
- **Lines 4-5**: `add(a, b)` returns sum.
- **Lines 7-8**: `subtract(a, b)` returns difference.
- **Lines 10-11**: `multiply(a, b)` returns product.
- **Lines 13-16**: `divide(a, b)` handles division and checks divide-by-zero.

### 2) Main calculator flow
- **Lines 18-21**: Prints title banner.
- **Lines 24-25**: Reads two numbers and converts them to `float`.
- **Lines 27-31**: Prints operation menu.
- **Line 33**: Takes user choice (`1/2/3/4`).

### 3) Choice handling with conditionals
- **Lines 35-37**: If choice is `1`, call `add`.
- **Lines 38-40**: If choice is `2`, call `subtract`.
- **Lines 41-43**: If choice is `3`, call `multiply`.
- **Lines 44-46**: If choice is `4`, call `divide`.
- **Lines 47-49**: Invalid input path with early return.

### 4) Result output
- **Line 51**: Prints final expression and result.

### 5) Program entry point and repeat loop
- **Lines 54-60**: Starts app and repeats until user enters anything other than `yes`.

## Example
```text
Enter first number: 10
Enter second number: 5
Enter choice (1/2/3/4): 3
10.0 * 5.0 = 50.0
```

## Optional Next Improvements
- Add operation history
- Add support for `%` and power operations
- Handle invalid numeric input with `try/except`
