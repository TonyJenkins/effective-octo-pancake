"""Task: Add all the integers in a list."""


def sum_numbers(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    print(f"Sum: {sum_numbers(numbers)}")
