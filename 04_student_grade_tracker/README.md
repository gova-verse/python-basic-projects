# Student Grade Tracker (Project 4)

A command-line tracker for student marks, grades, and class statistics.

## Run
```bash
python 04_student_grade_tracker/grade_tracker.py
```

## Program Flow (Line-by-Line Explanation)

### `grade_tracker.py`
- **Lines 1-2**: File header comments with covered concepts.
- **Lines 4-14**: `show_menu()` prints all menu options.
- **Lines 16-33**: `add_student(students)`:
  - Takes student name and normalizes format with `.title()`.
  - Validates empty and duplicate names.
  - Reads marks as float, enforces `0-100` range.
  - Stores student in dictionary and prints assigned letter grade.
- **Lines 35-47**: `get_grade(marks)` converts numeric marks to grade bands (`A+` to `F`).
- **Lines 49-61**: `view_students(students)`:
  - Handles empty data.
  - Sorts students by marks descending.
  - Prints formatted table with name, marks, and grade.
- **Lines 63-82**: `view_statistics(students)`:
  - Handles empty case.
  - Computes total, average, highest, and lowest marks.
  - Finds top and bottom students by mark.
  - Prints summary and class-level grade using average.
- **Lines 84-93**: `search_student(students)` prints one student's details if found.
- **Lines 95-104**: `delete_student(students)` removes a student by name if present.
- **Lines 106-127**: `main()`:
  - Creates empty `students` dictionary.
  - Runs menu loop.
  - Routes choices `1..6` to corresponding functions.
  - Exits on option `6`.
- **Lines 129-130**: Standard entry point.

## Key Data Structures
- `students`: dictionary in format `{student_name: marks}`.

## Suggested Improvements
- Add edit/update marks feature.
- Add import/export to CSV.
- Add per-subject grading (not just single mark).
