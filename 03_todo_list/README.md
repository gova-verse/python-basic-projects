# To-Do List App (Project 3)

A command-line to-do manager for adding, viewing, completing, and deleting tasks.

## Run
```bash
python 03_todo_list/todo.py
```

## Program Flow (Line-by-Line Explanation)

### `todo.py`
- **Lines 1-2**: File header comments with topic keywords.
- **Lines 4-12**: `show_menu()` prints the app menu and available actions.
- **Lines 14-21**: `view_tasks(tasks)`:
  - Shows title.
  - Handles empty task list.
  - Uses `enumerate(..., start=1)` to print numbered tasks.
  - Displays completion status using `✓` when done, otherwise `x`.
- **Lines 22-28**: `add_task(tasks)`:
  - Reads and trims task name.
  - Rejects empty input.
  - Appends a task dictionary: `{"name": name, "done": False}`.
- **Lines 29-42**: `mark_done(tasks)`:
  - Prevents action when list is empty.
  - Shows tasks first.
  - Reads task number safely with `int(...)` and `try/except`.
  - Validates range and marks selected task as completed.
- **Lines 43-56**: `delete_task(tasks)`:
  - Prevents action when list is empty.
  - Shows tasks and asks which one to remove.
  - Validates number and removes task via `pop(index)`.
- **Lines 58-77**: `main()`:
  - Initializes empty `tasks` list.
  - Runs loop showing menu and reading user choice.
  - Dispatches choices `1..5` to view/add/mark/delete/exit.
  - Handles invalid choices.
- **Lines 78-79**: Entry point that runs `main()` when file is executed directly.

## Key Data Structures
- `tasks`: list of dictionaries, each shaped like:
  - `name` (string)
  - `done` (boolean)

## Suggested Improvements
- Add save/load with JSON so tasks persist after exit.
- Add due dates and priority levels.
- Add filter views (all/completed/pending).
