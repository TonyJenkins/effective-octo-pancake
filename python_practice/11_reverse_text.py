"""Task: Reverse a string without changing the original."""


def reverse_text(text: str) -> str:
    return text[::-1]


if __name__ == "__main__":
    text = input("Enter some text: ")
    print(reverse_text(text))
