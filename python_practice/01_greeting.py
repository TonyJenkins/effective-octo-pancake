"""Task: Ask for a name and greet the user."""


def greet(name: str) -> str:
    return f"Hello, {name.strip()}!"


if __name__ == "__main__":
    name = input("What is your name? ")
    print(greet(name))
