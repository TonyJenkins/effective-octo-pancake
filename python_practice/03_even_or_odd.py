"""Task: Report whether an integer is even or odd."""


def even_or_odd(number: int) -> str:
    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(f"{number} is {even_or_odd(number)}.")
