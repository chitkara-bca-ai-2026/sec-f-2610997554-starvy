def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def format_number(n):
    if n == int(n):
        return int(n)
    return n


history = []

print("=" * 40)
print("   ENTERPRISE MODULAR UTILITY CALCULATOR")
print("=" * 40)

while True:
    print()
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")
    print()
    choice = input("Enter your choice (1-8): ")

    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

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
            result = modulus(a, b)
            symbol = "%"

        if result is None:
            print("[ERROR] Cannot divide by zero.")
        else:
            record = str(format_number(a)) + " " + symbol + " " + str(format_number(b)) + " = " + str(format_number(result))
            history.append(record)
            print("[RESULT]", record)

    elif choice == "6":
        base = float(input("Enter base number: "))
        exponent = input("Enter exponent (press Enter for default 2): ")

        if exponent == "":
            result = power(base)
            exp_shown = 2
        else:
            exp_value = float(exponent)
            result = power(base, exp_value)
            exp_shown = format_number(exp_value)

        record = str(format_number(base)) + " ^ " + str(exp_shown) + " = " + str(format_number(result))
        history.append(record)
        print("[RESULT]", record)

    elif choice == "7":
        print()
        print("--- Calculation History ---")
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for i in range(len(history)):
                print(str(i + 1) + ". " + history[i])

    elif choice == "8":
        print()
        print("Thank you for using the calculator. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 8.")