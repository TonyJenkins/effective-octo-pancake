"""Task: Generate the first n numbers in the Fibonacci sequence."""


def fibonacci(count: int) -> list[int]:
    if count < 0:
        raise ValueError("count must not be negative")
    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


if __name__ == "__main__":
    count = int(input("How many Fibonacci numbers? "))
    print(*fibonacci(count))
