# grade_tracker.py
# Concepts: dictionaries, functions, loops, string formatting, sorting, min/max

def show_menu():
    print("\n" + "=" * 40)
    print("        Student Grade Tracker")
    print("=" * 40)
    print("  1. Add student")
    print("  2. View all students")
    print("  3. View class statistics")
    print("  4. Search student")
    print("  5. Delete student")
    print("  6. Exit")
    print("=" * 40)

def add_student(students):
    name = input("\nEnter student name: ").strip().title()
    if name == "":
        print("Name cannot be empty!")
        return
    if name in students:
        print(f"Student '{name}' already exists!")
        return
    try:
        marks = float(input(f"Enter marks for {name} (0-100): "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return
        students[name] = marks
        grade = get_grade(marks)
        print(f"Student '{name}' added with marks {marks} — Grade: {grade}")
    except ValueError:
        print("Please enter valid marks!")

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def view_students(students):
    if len(students) == 0:
        print("\nNo students added yet!")
        return
    print("\n" + "-" * 40)
    print(f"  {'NAME':<20} {'MARKS':>6} {'GRADE':>6}")
    print("-" * 40)
    # sort students by marks in descending order
    sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    for name, marks in sorted_students:
        grade = get_grade(marks)
        print(f"  {name:<20} {marks:>6.1f} {grade:>6}")
    print("-" * 40)

def view_statistics(students):
    if len(students) == 0:
        print("\nNo students to calculate statistics!")
        return
    marks_list = list(students.values())
    total = sum(marks_list)
    average = total / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)

    # find names of top and bottom students
    top_student = max(students, key=students.get)
    bottom_student = min(students, key=students.get)

    print("\n--- Class Statistics ---")
    print(f"  Total students  : {len(students)}")
    print(f"  Average marks   : {average:.2f}")
    print(f"  Highest marks   : {highest} ({top_student})")
    print(f"  Lowest marks    : {lowest} ({bottom_student})")
    print(f"  Class grade     : {get_grade(average)}")

def search_student(students):
    name = input("\nEnter student name to search: ").strip().title()
    if name in students:
        marks = students[name]
        grade = get_grade(marks)
        print(f"\n  Name  : {name}")
        print(f"  Marks : {marks}")
        print(f"  Grade : {grade}")
    else:
        print(f"Student '{name}' not found!")

def delete_student(students):
    if len(students) == 0:
        print("\nNo students to delete!")
        return
    name = input("\nEnter student name to delete: ").strip().title()
    if name in students:
        del students[name]
        print(f"Student '{name}' deleted successfully!")
    else:
        print(f"Student '{name}' not found!")

def main():
    students = {}  # dictionary to store name:marks pairs

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            view_statistics(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Enter 1 to 6.")

if __name__ == "__main__":
    main()