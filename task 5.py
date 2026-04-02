
import re

while True:
    password = input("Enter your password: ")

    # Conditions
    length_ok = len(password) >= 8
    has_number = re.search(r"\d", password)
    has_upper = re.search(r"[A-Z]", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length_ok and has_number and has_upper and has_special:
        print("Strong Password")
        break
    else:
        print("Weak Password! Try again.\n")