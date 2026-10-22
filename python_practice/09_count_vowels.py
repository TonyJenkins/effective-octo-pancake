"""Task: Count the vowels in a piece of text."""


def count_vowels(text: str) -> int:
    return sum(character.casefold() in "aeiou" for character in text)


if __name__ == "__main__":
    text = input("Enter some text: ")
    print(f"Vowels: {count_vowels(text)}")
