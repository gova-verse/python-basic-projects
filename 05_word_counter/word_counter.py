# word_counter.py
# Concepts: file handling, string methods, dictionaries, sorting, functions

import os

def read_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found!")
        return None
    with open(filename, "r") as file:
        content = file.read()
    return content

def count_words(content):
    words = content.split()
    return len(words)

def count_sentences(content):
    sentences = [s.strip() for s in content.replace("?", ".").replace("!", ".").split(".") if s.strip()]
    return len(sentences)

def count_unique_words(content):
    words = content.lower().split()
    cleaned = []
    for word in words:
        word = word.strip(".,!?;:\"'()")
        if word:
            cleaned.append(word)
    unique = set(cleaned)
    return len(unique), unique

def word_frequency(content):
    words = content.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:\"'()")
        if word:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def show_menu():
    print("\n" + "=" * 40)
    print("           Word Counter App")
    print("=" * 40)
    print("  1. Analyze a file")
    print("  2. Analyze custom text")
    print("  3. Exit")
    print("=" * 40)

def analyze_content(content):
    total_words = count_words(content)
    total_chars = len(content)
    total_chars_no_space = len(content.replace(" ", "").replace("\n", ""))
    total_sentences = count_sentences(content)
    total_lines = len(content.splitlines())
    unique_count, unique_words = count_unique_words(content)
    freq = word_frequency(content)

    print("\n--- Analysis Results ---")
    print(f"  Total words         : {total_words}")
    print(f"  Total characters    : {total_chars}")
    print(f"  Chars (no spaces)   : {total_chars_no_space}")
    print(f"  Total sentences     : {total_sentences}")
    print(f"  Total lines         : {total_lines}")
    print(f"  Unique words        : {unique_count}")

    print("\n--- Top 10 Most Used Words ---")
    print(f"  {'WORD':<20} {'COUNT':>5}")
    print("  " + "-" * 25)
    for word, count in freq[:10]:
        print(f"  {word:<20} {count:>5}")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            filename = input("\nEnter filename (e.g. sample.txt): ").strip()
            content = read_file(filename)
            if content:
                analyze_content(content)
        elif choice == "2":
            print("\nEnter your text (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = " ".join(lines)
            if content.strip():
                analyze_content(content)
            else:
                print("No text entered!")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Enter 1 to 3.")

if __name__ == "__main__":
    main()