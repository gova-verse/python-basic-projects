# Word Counter App (Project 5)

A command-line text analysis tool for counting words, sentences, lines, and frequencies.

## Run
```bash
python 05_word_counter/word_counter.py
```

## Program Flow (Line-by-Line Explanation)

### `word_counter.py`
- **Lines 1-2**: File header comments.
- **Line 4**: Imports `os` for file existence checks.
- **Lines 6-12**: `read_file(filename)`:
  - Verifies file exists.
  - Reads text content and returns it.
  - Returns `None` with an error message if missing.
- **Lines 14-16**: `count_words(content)` splits text and returns word count.
- **Lines 18-20**: `count_sentences(content)` normalizes `?` and `!` to `.`, splits into sentence-like chunks, returns count.
- **Lines 22-30**: `count_unique_words(content)`:
  - Lowercases words.
  - Strips punctuation.
  - Builds cleaned list and returns `(count, set_of_unique_words)`.
- **Lines 32-43**: `word_frequency(content)`:
  - Lowercases and cleans words.
  - Builds frequency dictionary.
  - Returns list of `(word, count)` sorted by descending count.
- **Lines 45-52**: `show_menu()` displays analysis mode options.
- **Lines 54-75**: `analyze_content(content)`:
  - Calls helper functions to compute all metrics.
  - Prints totals for words/chars/sentences/lines/unique words.
  - Prints top 10 most frequent words.
- **Lines 77-104**: `main()`:
  - Runs menu loop.
  - Option 1: analyze file input.
  - Option 2: analyze custom multi-line text.
  - Option 3: exit.
  - Handles invalid choices.
- **Lines 106-107**: Entry point.

## Key Data Structures
- `frequency` dictionary for counts.
- `set` for unique words.
- `list` of lines for custom multi-line user input.

## Suggested Improvements
- Remove stop words (e.g., "the", "is").
- Add stemming/lemmatization.
- Add export of analysis results to CSV or JSON.
