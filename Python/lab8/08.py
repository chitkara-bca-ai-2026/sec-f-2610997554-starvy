print("=" * 50)
print("            SCHOOL RESULT PROCESSING")
print("=" * 50)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print()
print("--- Enter marks for 5 Subjects (0-100) ---")

total = 0
failed = False

for i in range(1, 6):
    marks = float(input("Enter marks for Subject " + str(i) + ": "))
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100")
        exit()
    if marks < 40:
        failed = True
    total = total + marks

percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

print()
print("=" * 50)
print("              STUDENT REPORT CARD")
print("=" * 50)
print("  Student Name :", name)
print("  Roll Number  :", roll)
print("-" * 50)
print("  Total Marks  :", total, "/ 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print("  Result       :", result)
print("  Grade        :", grade)
print("  Remarks      :", remark)
print("=" * 50)