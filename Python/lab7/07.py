print("=" * 40)
print("     CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Year must be greater than 0")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            reason = "Century year divisible by 400"
        else:
            status = "COMMON YEAR"
            reason = "Century year not divisible by 400"
    else:
        if year % 4 == 0:
            status = "LEAP YEAR"
            reason = "Divisible by 4 and not a century year"
        else:
            status = "COMMON YEAR"
            reason = "Not divisible by 4"

    if status == "LEAP YEAR":
        days_in_year = 366
        days_in_february = 29
    else:
        days_in_year = 365
        days_in_february = 28

    print()
    print("-" * 40)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days_in_year, "days")
    print("Days in February:", days_in_february, "days")
    print("Reason:", reason)
    print("-" * 40)