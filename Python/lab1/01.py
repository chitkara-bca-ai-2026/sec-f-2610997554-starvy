tuition_fee=float(input("Enter Tuition Fee: "))
lab_fee=float(input("Enter Lab Fee: "))
library_fee=float(input("Enter Library Fee: "))
exam_fee=float(input("Enter Exam Fee: "))
discount=float(input("Enter Discount Amount: "))
print()
               
total_fee=tuition_fee+lab_fee+library_fee+exam_fee
fee_after_discount=total_fee-discount
annual_fee=fee_after_discount*2
monthly_fee=annual_fee/12
print(f"Tuition Fee: {tuition_fee}\nLab Fee: {lab_fee}\nLibrary Fee: {library_fee}\nExam Fee: {exam_fee}\nTotal Fee: {total_fee}\nDiscount : {discount}\nFee after Discount: {fee_after_discount}\nAnnual Fee: {annual_fee}\nMonthly Installment: {monthly_fee}")