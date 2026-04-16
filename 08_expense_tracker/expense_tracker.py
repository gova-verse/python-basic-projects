# expense_tracker.py
# Concepts: CSV file handling, data persistence, classes, datetime, file read/write

import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Health", "Education", "Other"]

class Expense:
    def __init__(self, date, category, description, amount):
        self.date        = date
        self.category    = category
        self.description = description
        self.amount      = float(amount)

    def to_list(self):
        # converts object to list for CSV writing
        return [self.date, self.category, self.description, self.amount]

    def display(self):
        print(f"  {self.date:<12} {self.category:<12} {self.description:<20} Rs.{self.amount:.2f}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_from_file()

    def load_from_file(self):
        # load existing expenses from CSV on startup
        if not os.path.exists(FILENAME):
            return
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                if row:
                    expense = Expense(row[0], row[1], row[2], row[3])
                    self.expenses.append(expense)
        print(f"Loaded {len(self.expenses)} expense(s) from file.")

    def save_to_file(self):
        # save all expenses to CSV
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
            for expense in self.expenses:
                writer.writerow(expense.to_list())

    def add_expense(self):
        print("\n--- Add New Expense ---")
        print("\nCategories:")
        for i, cat in enumerate(CATEGORIES, start=1):
            print(f"  {i}. {cat}")
        try:
            cat_choice = int(input("\nSelect category (1-7): "))
            if cat_choice < 1 or cat_choice > len(CATEGORIES):
                print("Invalid category!")
                return
            category = CATEGORIES[cat_choice - 1]
        except ValueError:
            print("Please enter a valid number!")
            return

        description = input("Description: ").strip()
        if not description:
            print("Description cannot be empty!")
            return

        try:
            amount = float(input("Amount (Rs.): "))
            if amount <= 0:
                print("Amount must be greater than zero!")
                return
        except ValueError:
            print("Please enter a valid amount!")
            return

        date = datetime.now().strftime("%Y-%m-%d")
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        self.save_to_file()
        print(f"Expense of Rs.{amount:.2f} added successfully!")

    def view_all(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        print("\n--- All Expenses ---")
        print(f"  {'DATE':<12} {'CATEGORY':<12} {'DESCRIPTION':<20} {'AMOUNT'}")
        print("  " + "-" * 55)
        for expense in self.expenses:
            expense.display()
        print("  " + "-" * 55)
        total = sum(e.amount for e in self.expenses)
        print(f"  {'TOTAL':<44} Rs.{total:.2f}")

    def view_by_category(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        print("\n--- Expenses by Category ---")
        category_totals = {}
        for expense in self.expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount
        sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        print(f"\n  {'CATEGORY':<20} {'TOTAL'}")
        print("  " + "-" * 30)
        for category, total in sorted_cats:
            print(f"  {category:<20} Rs.{total:.2f}")

    def view_statistics(self):
        if not self.expenses:
            print("\nNo expenses recorded yet!")
            return
        amounts = [e.amount for e in self.expenses]
        total   = sum(amounts)
        average = total / len(amounts)
        highest = max(amounts)
        lowest  = min(amounts)
        print("\n--- Statistics ---")
        print(f"  Total expenses  : {len(self.expenses)}")
        print(f"  Total spent     : Rs.{total:.2f}")
        print(f"  Average expense : Rs.{average:.2f}")
        print(f"  Highest expense : Rs.{highest:.2f}")
        print(f"  Lowest expense  : Rs.{lowest:.2f}")

    def delete_expense(self):
        if not self.expenses:
            print("\nNo expenses to delete!")
            return
        self.view_all()
        try:
            number = int(input("\nEnter expense number to delete: "))
            if number < 1 or number > len(self.expenses):
                print("Invalid number!")
                return
            removed = self.expenses.pop(number - 1)
            self.save_to_file()
            print(f"Expense '{removed.description}' deleted!")
        except ValueError:
            print("Please enter a valid number!")


def show_menu(tracker):
    print("\n" + "=" * 40)
    print("         Expense Tracker")
    print("=" * 40)
    print("  1. Add expense")
    print("  2. View all expenses")
    print("  3. View by category")
    print("  4. View statistics")
    print("  5. Delete expense")
    print("  6. Exit")
    print("=" * 40)
    total = sum(e.amount for e in tracker.expenses)
    print(f"  Total spent so far: Rs.{total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        show_menu(tracker)
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_all()
        elif choice == "3":
            tracker.view_by_category()
        elif choice == "4":
            tracker.view_statistics()
        elif choice == "5":
            tracker.delete_expense()
        elif choice == "6":
            print("\nGoodbye! Keep tracking your expenses!")
            break
        else:
            print("Invalid choice! Enter 1 to 6.")

if __name__ == "__main__":
    main()