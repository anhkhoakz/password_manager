import secrets
import string
import pyperclip


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    password = generate_password()
    print("Generated Password:", password)
    pyperclip.copy(password)


if __name__ == "__main__":
    main()
