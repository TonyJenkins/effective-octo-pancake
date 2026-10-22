"""Task: Count the words in a sentence, ignoring extra whitespace."""


def count_words(sentence: str) -> int:
    return len(sentence.split())


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(f"Words: {count_words(sentence)}")
