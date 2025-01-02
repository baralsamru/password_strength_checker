import re
import string

# List of common weak passwords (this could be expanded or sourced from a file)
common_passwords = ['123456', 'password', 'hello', 'qwerty', 'letmein', 'password123']

def check_password_strength(password):
    # Check if the password is in the common passwords list
    if password.lower() in common_passwords:
        return "Password is too common. Choose a more unique password."

    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return "Password too short. It should be at least 8 characters."

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check if the password contains at least one digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."

    # Check if the password contains common sequences (e.g., 123, abc, qwerty)
    if re.search(r'(123|abc|qwerty)', password):
        return "Password contains a predictable sequence. Use something more random."

    # Check if the password lacks variety or randomness
    if len(set(password)) < 5:  # Password has less than 5 unique characters (low entropy)
        return "Password lacks variety. It should contain a mix of characters."

    return "Password is strong."

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)




