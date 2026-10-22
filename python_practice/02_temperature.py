"""Task: Convert a temperature in Celsius to Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    celsius = float(input("Temperature in Celsius: "))
    print(f"{celsius:g}°C is {celsius_to_fahrenheit(celsius):g}°F")
