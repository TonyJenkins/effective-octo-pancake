"""Task: Determine whether an integer greater than one is prime."""


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    answer = "prime" if is_prime(number) else "not prime"
    print(f"{number} is {answer}.")
