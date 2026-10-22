"""Task: Find the largest of three numbers without using max()."""


def largest_of_three(first: float, second: float, third: float) -> float:
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest


if __name__ == "__main__":
    numbers = [float(input(f"Number {i}: ")) for i in range(1, 4)]
    print(f"Largest: {largest_of_three(*numbers):g}")
