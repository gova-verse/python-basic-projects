# Contact Book (Project 7)

A command-line contact manager using Object-Oriented Programming (OOP).

## Run
```bash
python 07_contact_book/contact_book.py
```

## Program Flow (Line-by-Line Explanation)

### `contact_book.py`
- **Line 1**: File label comment.
- **Line 2**: Comment listing OOP concepts used.

### `Contact` class
- **Lines 4-5**: Declares `Contact` class and constructor.
- **Lines 6-9**: Constructor stores `name`, `phone`, and `email` on the object.
- **Lines 11-15**: `display()` prints one contact's details in a readable format.
- **Lines 17-23**: `update(phone=None, email=None)` updates only provided fields and confirms update.

### `ContactBook` class
- **Lines 26-29**: Constructor initializes `self.contacts` as empty list.
- **Lines 31-38**: `add_contact(...)`:
  - Prevents duplicates using `find_contact`.
  - Creates `Contact` object and appends to list.
- **Lines 40-45**: `find_contact(name)` performs case-insensitive search and returns contact or `None`.
- **Lines 47-56**: `view_all()`:
  - Handles empty list.
  - Prints table header and all contacts with numbering.
- **Lines 57-64**: `search_contact(name)` prints found contact or not-found message.
- **Lines 65-77**: `update_contact(name)`:
  - Finds contact, exits if missing.
  - Prompts for new phone/email.
  - Keeps old values when user presses Enter.
- **Lines 78-85**: `delete_contact(name)` removes matching contact if present.
- **Lines 86-87**: `total_contacts()` returns number of saved contacts.

### Menu + input helpers
- **Lines 90-102**: `show_menu()` prints menu and current total contacts (`book.total_contacts()`).
- **Lines 104-110**: `get_input(prompt, allow_empty=False)` enforces non-empty input unless allowed.

### Main loop
- **Lines 112-145**: `main()`:
  - Shows menu.
  - Reads choice.
  - Routes to add/view/search/update/delete/exit actions.
  - Handles invalid choice with message.
- **Lines 147-148**: Creates one global `ContactBook` instance (`book`).
- **Lines 150-151**: Entry point that runs `main()`.

## Key Data Structures
- `Contact` objects for each person.
- `book.contacts` list storing all contact objects.

## Suggested Improvements
- Add phone/email format validation.
- Save contacts to JSON/CSV for persistence.
- Add duplicate checks for phone numbers too.
