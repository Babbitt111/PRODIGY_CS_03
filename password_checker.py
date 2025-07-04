import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing number": digit_error,
        "Missing special character": special_char_error
    }

    failed_criteria = [msg for msg, failed in errors.items() if failed]

    if len(failed_criteria) == 0:
        strength = "Strong 💪"
    elif len(failed_criteria) <= 2:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, failed_criteria

# --- User Interface ---
password = input("🔐 Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for issue in feedback:
        print(f" - {issue}")
else:
    print("✅ Your password meets all recommended criteria.")