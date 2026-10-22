"""Task: Find the second-largest distinct number in a list."""


def second_largest(numbers: list[float]) -> float:
    distinct = sorted(set(numbers))
    if len(distinct) < 2:
        raise ValueError("provide at least two distinct numbers")
    return distinct[-2]


if __name__ == "__main__":
    numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]
    print(f"Second-largest: {second_largest(numbers):g}")
