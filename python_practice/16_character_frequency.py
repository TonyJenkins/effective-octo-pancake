"""Task: Count how often each non-whitespace character appears."""


def character_frequency(text: str) -> dict[str, int]:
    counts = {}
    for character in text:
        if not character.isspace():
            counts[character] = counts.get(character, 0) + 1
    return counts


if __name__ == "__main__":
    text = input("Enter some text: ")
    print(character_frequency(text))
