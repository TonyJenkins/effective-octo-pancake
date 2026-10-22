"""Task: Apply a percentage discount to a non-negative price."""


def discounted_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("price must not be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)


if __name__ == "__main__":
    price = float(input("Original price: "))
    discount = float(input("Discount percentage: "))
    print(f"Price after discount: {discounted_price(price, discount):.2f}")
