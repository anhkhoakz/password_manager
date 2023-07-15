import secrets
import requests
import os
import pyperclip


def get_words():
    """Gets a list of words from the EFF wordlist."""
    url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        lines = data.split("\n")
        words = []
        for line in lines:
            if line:
                line = line.split("\t")
                word = line[1]
                words.append(word)
        return words
    else:
        return []


def generate_passphrase(words, length):
    """Generates a passphrase of the specified length."""
    passPhrase = []
    for _ in range(length):
        randomWord = secrets.choice(words)
        passPhrase.append(randomWord)
    return passPhrase


def save_words(words):
    """Saves the list of words to a file."""
    filename = "words.txt"
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")


def load_words():
    """Loads the list of words from a file."""
    filename = "words.txt"
    words = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for word in f:
                words.append(word.strip())
    return words


def main():
    """The main function."""
    words = load_words()
    if not words:
        words = get_words()
        save_words(words)
    passphrase = generate_passphrase(words, 6)
    print(passphrase)
    pyperclip.copy(str(passphrase))


if __name__ == "__main__":
    main()
