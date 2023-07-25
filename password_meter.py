import re


def password_strength(password):
    """Returns the strength of a password."""

    strength = 0

    # Check the length of the password.
    if len(password) < 6:
        return "Weak"
    elif len(password) < 12:
        strength += 1
    elif len(password) < 16:
        strength += 2
    else:
        strength += 3

    # Check for the presence of lowercase letters, uppercase letters, numbers, and symbols.
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*()_+-]", password):
        strength += 1

    # Check the complexity of the password.
    if re.search("[a-z]{2,}", password):
        strength += 1
    if re.search("[A-Z]{2,}", password):
        strength += 1
    if re.search("[0-9]{2,}", password):
        strength += 1
    if re.search("[!@#$%^&*()_+-]{2,}", password):
        strength += 1

    if strength == 0:
        return "Weak"
    elif strength == 1 or strength == 2:
        return "Good"
    else:
        return "Strong"


def main():
    """Prompts the user for a password and then prints the strength."""

    password = input("Enter a password: ")
    strength = password_strength(password)
    print("The strength of your password is:", strength)


if __name__ == "__main__":
    main()
