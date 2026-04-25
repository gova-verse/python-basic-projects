# quiz_app.py
# Concepts: try/except, error handling, lists of dicts, functions, score logic, enumerate

import time
import random

QUESTIONS = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "define", "function"],
        "answer": "def"
    },
    {
        "question": "What data type is the result of: type([])?",
        "options": ["tuple", "set", "dict", "list"],
        "answer": "list"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()"
    },
    {
        "question": "What does len('Python') return?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    },
    {
        "question": "What is the correct way to create a dictionary?",
        "options": ["d = []", "d = ()", "d = {}", "d = <>"],
        "answer": "d = {}"
    },
    {
        "question": "Which loop is used when the number of iterations is unknown?",
        "options": ["for loop", "while loop", "do loop", "repeat loop"],
        "answer": "while loop"
    },
    {
        "question": "What does the 'import' keyword do?",
        "options": [
            "Creates a new file",
            "Loads an external module",
            "Defines a class",
            "Starts a loop"
        ],
        "answer": "Loads an external module"
    },
    {
        "question": "What is the output of bool(0)?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False"
    }
]

def show_welcome():
    print("=" * 45)
    print("         Python Knowledge Quiz")
    print("=" * 45)
    print("  Rules:")
    print("  - 10 questions total")
    print("  - 4 options per question")
    print("  - Type the number of your answer")
    print("  - No time limit")
    print("=" * 45)

def ask_question(question_data, number, total):
    print(f"\nQuestion {number} of {total}")
    print("-" * 45)
    print(f"  {question_data['question']}")
    print()

    # shuffle options so answer position changes each time
    options = question_data["options"][:]
    random.shuffle(options)

    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    # get valid answer from user
    while True:
        try:
            choice = int(input("\n  Your answer (1-4): "))
            if choice < 1 or choice > 4:
                print("  Please enter a number between 1 and 4!")
                continue
            break
        except ValueError:
            print("  Invalid input! Please enter a number 1 to 4.")

    selected = options[choice - 1]
    correct  = question_data["answer"]

    if selected == correct:
        print("  Correct! Well done!")
        return True
    else:
        print(f"  Wrong! The correct answer was: {correct}")
        return False

def get_grade(score, total):
    percentage = (score / total) * 100
    if percentage == 100:
        return "A+", "Perfect score! Outstanding!"
    elif percentage >= 80:
        return "A", "Excellent work!"
    elif percentage >= 60:
        return "B", "Good job!"
    elif percentage >= 40:
        return "C", "Keep practicing!"
    else:
        return "F", "More study needed!"

def show_results(score, total, wrong_answers, time_taken):
    percentage = (score / total) * 100
    grade, message = get_grade(score, total)

    print("\n" + "=" * 45)
    print("              Quiz Results")
    print("=" * 45)
    print(f"  Score         : {score} / {total}")
    print(f"  Percentage    : {percentage:.1f}%")
    print(f"  Grade         : {grade}")
    print(f"  Time taken    : {time_taken:.1f} seconds")
    print(f"  Message       : {message}")

    if len(wrong_answers) > 0:
        print("\n--- Questions You Got Wrong ---")
        for i, qa in enumerate(wrong_answers, start=1):
            print(f"\n  {i}. {qa['question']}")
            print(f"     Correct answer: {qa['answer']}")

def main():
    show_welcome()
    input("\nPress Enter to start the quiz...")

    # shuffle questions for variety
    questions = QUESTIONS[:]
    random.shuffle(questions)

    score        = 0
    wrong_answers = []
    start_time   = time.time()

    for i, question in enumerate(questions, start=1):
        is_correct = ask_question(question, i, len(questions))
        if is_correct:
            score += 1
        else:
            wrong_answers.append(question)
        # small pause between questions
        time.sleep(0.5)

    end_time   = time.time()
    time_taken = end_time - start_time

    show_results(score, len(questions), wrong_answers, time_taken)

    print("\n" + "=" * 45)
    again = input("Play again? (yes/no): ").lower().strip()
    if again == "yes":
        main()
    else:
        print("\nThanks for playing! Keep learning Python!")

if __name__ == "__main__":
    main()