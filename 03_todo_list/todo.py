#todo.py
#concepts: lists, functions, while loop, string methods, enumerate

def show_menu():
    print("\n"  + "=" * 35)
    print("      To-Do List App")
    print("=" * 35)
    print("  1.View All Tasks")
    print("  2. Add a task")
    print("   3. Mark task as done")
    print(" 4.Delete a task")
    print("=" * 35)

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if len (tasks) ==0:
        print("No tasks yet! Add one.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else"x"
        print(f"  {index}. [{status}]  {task['name']}")
def add_task(tasks):
    name = input("\nEnter task name: ").strip()
    if name == "":
        print("Task name cannot be empty!")
        return
    tasks.append({"name": name, "done":False})
    print(f"Task ,{name} added successfully")
def mark_done(tasks):
    if len(tasks) == 0:
        print("No tasks to mark!")
        return
    view_tasks(tasks)
    try:
        number = int(input("\nEnter task number to mark as done: "))
        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return
        tasks[number - 1]["done"] = True
        print(f"Task '{tasks[number - 1]['name']}' marked as done")
    except ValueError :
        print("Please enter a valid Number !")
def delete_task(tasks):
    if len(tasks) == 0:
        print("no tasks to delete!")
        return
    view_tasks(tasks)
    try:
        number = int(input("\nEnter task number to delete: "))
        if number < 1 or number > len(tasks):
            return
        removed = tasks.pop(number - 1)
        print(f"Task '{removed['name']} 'deleted!")
        return
    except ValueError:
        print('Please enter a valid number!')

def main():
    tasks = [] #empty list to store all tasks
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":   
            print("\nGoodbye: Stay productive!")
            break
        else:
            print("Invalid choice ! Please enter 1 to 5.")
if __name__ == "__main__":
    main()
        