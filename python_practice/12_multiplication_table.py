"""Task: Print a multiplication table from 1 through 10."""


def multiplication_table(number: int) -> list[str]:
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, 11)]


if __name__ == "__main__":
    number = int(input("Which multiplication table? "))
    print("\n".join(multiplication_table(number)))
