import os


def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("[SUCCESS] Notes successfully saved to '" + filename + "'.")


def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    return "No notes file exists yet."


print("=" * 40)
print("      STUDENT NOTES MANAGEMENT SYSTEM")
print("=" * 40)

while True:
    print()
    print("Select an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    print()
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        notes = input("Enter notes to save: ")
        write_notes("notes.txt", notes)

    elif choice == "2":
        print("--- Notes Content (notes.txt) ---")
        print(read_notes("notes.txt"))

    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 3.")