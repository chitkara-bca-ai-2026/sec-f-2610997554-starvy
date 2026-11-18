def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("=" * 40)
print("     MATHEMATICS LEARNING TOOL")
print("=" * 40)

while True:
    print()
    print("Select an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")
    print()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("[ERROR] Number must be non-negative.")
        else:
            print("[RESULT] Factorial of", n, "=", factorial(n))

    elif choice == "2":
        terms = int(input("Enter number of terms: "))
        if terms <= 0:
            print("[ERROR] Number of terms must be greater than 0.")
        else:
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print("[RESULT] Fibonacci Series:", series)

    elif choice == "3":
        print()
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 3.")