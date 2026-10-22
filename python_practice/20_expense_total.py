"""Task: Add expenses grouped by category and display category totals."""


def expense_totals(expenses: list[tuple[str, float]]) -> dict[str, float]:
    totals = {}
    for category, amount in expenses:
        if amount < 0:
            raise ValueError("expense amounts must not be negative")
        totals[category] = totals.get(category, 0) + amount
    return totals


if __name__ == "__main__":
    expenses = []
    while True:
        category = input("Category (or Enter to finish): ").strip()
        if not category:
            break
        amount = float(input("Amount: "))
        expenses.append((category, amount))

    totals = expense_totals(expenses)
    for category, amount in sorted(totals.items()):
        print(f"{category}: {amount:.2f}")
    print(f"Total: {sum(totals.values()):.2f}")
