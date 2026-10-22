"""Task: Build an acronym from the first letter of each word."""


def acronym(phrase: str) -> str:
    return "".join(word[0].upper() for word in phrase.split() if word)


if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    print(acronym(phrase))
