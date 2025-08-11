'''
Task # 03
Password Complexity Checker
'''
import re

def password_strength(password):
    # Criteria counters
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count met criteria
    criteria_met = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Determine strength
    if length_error:
        feedback = "❌ Password must be at least 8 characters long."
    else:
        feedback = "✅ Password length is good."

    if uppercase_error:
        feedback += "\n❌ Add at least one uppercase letter."
    else:
        feedback += "\n✅ Uppercase letter present."

    if lowercase_error:
        feedback += "\n❌ Add at least one lowercase letter."
    else:
        feedback += "\n✅ Lowercase letter present."

    if digit_error:
        feedback += "\n❌ Add at least one number."
    else:
        feedback += "\n✅ Number present."

    if special_char_error:
        feedback += "\n❌ Add at least one special character."
    else:
        feedback += "\n✅ Special character present."

    # Strength rating
    if criteria_met <= 2:
        strength = "Weak"
    elif 3 <= criteria_met < 5:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

# Interactive check
while True:
    pwd = input("\nEnter a password to check strength (or 'exit' to quit): ")
    if pwd.lower() == "exit":
        print("Goodbye! Stay secure. 🔐")
        break

    strength, feedback = password_strength(pwd)
    print(f"\nPassword Strength: {strength}")
    print(feedback)