import os


def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print("[SUCCESS] New entry logged to '" + filename + "'.")


def display_log(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    print("=" * 15 + " DAILY LOG BOOK " + "=" * 15)
    count = 0
    for line in lines:
        count = count + 1
        print("[" + str(count).zfill(2) + "] " + line.strip())
    print()
    print("Total Logged Entries:", count)
    print("=" * 46)


filename = "daily_log.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("09:00 AM - System server startup verified.\n")
        file.write("10:30 AM - Morning attendance synchronized.\n")
        file.write("02:15 PM - Network security patch applied.\n")

print("=" * 40)
print("          OFFICE DAILY LOG BOOK")
print("=" * 40)

while True:
    print()
    print("Select an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")
    print()
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 3.")