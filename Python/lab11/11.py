username = input("Enter your username: ")
password = input("Enter your password: ")

has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

valid = True

print("=" * 40)
print("PASSWORD VALIDATION REPORT")
print("=" * 40)
print("Username:", username)
print("Password:", "*" * len(password))

print()
print("--- Validation Rules ---")

if len(password) >= 8:
    print("[PASS] Minimum 8 characters (" + str(len(password)) + " characters)")
else:
    print("[FAIL] Minimum 8 characters (" + str(len(password)) + " characters)")
    valid = False

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")
    valid = False

if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")
    valid = False

print()
print("--- Result ---")

if valid:
    print("Password is VALID!")
    print("Account created successfully for " + username + "!")
else:
    print("Password is INVALID!")

print()
print("=" * 40)