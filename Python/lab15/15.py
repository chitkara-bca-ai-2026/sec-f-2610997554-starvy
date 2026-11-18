students = {
    "101": {"Name": "Aman",  "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya",  "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}
print("=" * 50)
print("     STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=" * 50)
while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    choice = input("\nEnter your choice (1-7): ")
    if choice == "1":
        print("\n--- Enrolled Student Records ---")
        for roll, info in students.items():
            print("Roll No:", roll,
                  "| Name:", info["Name"],
                  "| Branch:", info["Branch"],
                  "| Sem:", info["Semester"],
                  "| Marks:", info["Marks"])

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll) 
        if student != None:
            print("\n[FOUND] Record for Roll No", roll)
            print("  Name     :", student["Name"])
            print("  Branch   :", student["Branch"])
            print("  Semester :", student["Semester"])
            print("  Marks    :", student["Marks"])
        else:
            print("[ERROR] Student not found.")

    elif choice == "3":
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("[ERROR] Roll Number already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3]
            }
            print("[SUCCESS] Student", name, "(Roll No:", roll, ") registered successfully.")

    elif choice == "4":
        print("\n--- Update Student Details ---")
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            print("What do you want to update?")
            print("1. Name")
            print("2. Branch")
            print("3. Semester")
            print("4. Marks")
            option = input("Enter option (1-4): ")

            if option == "1":
                students[roll]["Name"] = input("Enter new Name: ")
                print("[SUCCESS] Name updated.")

            elif option == "2":
                students[roll]["Branch"] = input("Enter new Branch: ")
                print("[SUCCESS] Branch updated.")

            elif option == "3":
                students[roll]["Semester"] = input("Enter new Semester: ")
                print("[SUCCESS] Semester updated.")

            elif option == "4":
                print("Enter new marks for 3 subjects:")
                m1 = int(input("  Subject 1: "))
                m2 = int(input("  Subject 2: "))
                m3 = int(input("  Subject 3: "))
                students[roll]["Marks"] = [m1, m2, m3]
                print("[SUCCESS] Marks updated.")

            else:
                print("[ERROR] Invalid option.")
        else:
            print("[ERROR] Student not found.")

    elif choice == "5":
        print("\n--- Academic Performance ---")
        roll = input("Enter Roll Number: ")

        if roll in students:
            marks = students[roll]["Marks"]
            total = marks[0] + marks[1] + marks[2]
            percentage = total / 3
            if percentage >= 40:
                result = "PASS"
            else:
                result = "FAIL"
            print("Name        :", students[roll]["Name"])
            print("Total Marks :", total)
            print("Percentage  :", percentage , "%")
            print("Result      :", result)
        else:
            print("[ERROR] Student not found.")

    elif choice == "6":
        print("\n--- Delete Student Record ---")
        roll = input("Enter Roll Number to delete: ")

        if roll in students:
            students.pop(roll)
            print("[SUCCESS] Record deleted.")
        else:
            print("[ERROR] Student not found.")

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")