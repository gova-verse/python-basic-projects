# calculator.py
# Concepts: input/output, type casting, functions, conditionals, operators

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("=" * 30)
    print("       Simple Calculator")
    print("=" * 30)

    # input() always returns a string, so we cast to float
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nSelect operation:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        result = add(a, b)
        symbol = "+"
    elif choice == "2":
        result = subtract(a, b)
        symbol = "-"
    elif choice == "3":
        result = multiply(a, b)
        symbol = "*"
    elif choice == "4":
        result = divide(a, b)
        symbol = "/"
    else:
        print("Invalid choice!")
        return

    print(f"\n{a} {symbol} {b} = {result}")

# Entry point — this runs only when you execute this file directly
if __name__ == "__main__":
    while True:
        calculator()
        again = input("\nCalculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break