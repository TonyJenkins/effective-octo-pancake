"""Task: Calculate the factorial of a non-negative integer."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print(f"{number}! = {factorial(number)}")
