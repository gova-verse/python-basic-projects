# Expense Tracker (Project 8)

A command-line expense tracker with CSV-based persistence.

## Run
```bash
python 08_expense_tracker/expense_tracker.py
```

## Program Flow (Line-by-Line Explanation)

### `expense_tracker.py`
- **Line 1**: File label comment.
- **Line 2**: Comment listing key concepts.
- **Lines 4-6**: Imports `csv`, `os`, and `datetime`.
- **Line 8**: Defines CSV filename constant (`expenses.csv`).
- **Line 9**: Defines allowed expense categories.

### `Expense` class
- **Lines 11-12**: Class + constructor declaration.
- **Lines 13-16**: Stores date/category/description/amount; converts amount to float.
- **Lines 18-20**: `to_list()` converts object to list row for CSV writes.
- **Lines 22-23**: `display()` prints one formatted expense row.

### `ExpenseTracker` class
- **Lines 26-29**: Constructor initializes `self.expenses` and loads existing data from file.
- **Lines 31-43**: `load_from_file()`:
  - Exits if CSV doesn't exist.
  - Reads CSV rows, skips header, builds `Expense` objects, appends to list.
  - Prints loaded count.
- **Lines 44-50**: `save_to_file()` writes header and all current expenses to CSV.
- **Lines 52-86**: `add_expense()`:
  - Displays categories.
  - Validates category choice.
  - Validates non-empty description.
  - Validates numeric positive amount.
  - Uses today's date (`YYYY-MM-DD`).
  - Appends expense, saves file, confirms success.
- **Lines 87-99**: `view_all()`:
  - Handles empty state.
  - Prints table of all expenses.
  - Calculates and prints total amount spent.
- **Lines 100-116**: `view_by_category()`:
  - Aggregates totals per category using dictionary.
  - Sorts categories by highest total and prints summary.
- **Lines 117-132**: `view_statistics()` computes total/average/highest/lowest expense amounts.
- **Lines 133-147**: `delete_expense()`:
  - Displays list.
  - Removes selected expense by number.
  - Saves updated data.

### Menu + app loop
- **Lines 150-163**: `show_menu(tracker)` prints options and running total.
- **Lines 165-186**: `main()` creates tracker and routes user menu choices to tracker methods.
- **Lines 188-189**: Standard entry point.

## Key Data Structures
- `Expense` objects in `tracker.expenses` list.
- Category totals dictionary in `view_by_category()`.

## Suggested Improvements
- Add monthly and date-range reports.
- Add edit-expense feature.
- Add currency configuration and export options.
