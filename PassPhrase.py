import random
import requests


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
        randomWord = random.choice(words)
        passPhrase.append(randomWord)
    return passPhrase


def main():
    """The main function."""
    words = get_words()
    passphrase = generate_passphrase(words, 6)
    print(passphrase)


if __name__ == "__main__":
    main()
