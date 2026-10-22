"""Task: Check whether text reads the same forwards and backwards."""


def is_palindrome(text: str) -> bool:
    normalized = "".join(character.casefold() for character in text if character.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    text = input("Enter some text: ")
    print("Palindrome." if is_palindrome(text) else "Not a palindrome.")
