"""Task: Remove duplicates from a list while keeping the original order."""


def unique_items(items: list[str]) -> list[str]:
    result = []
    seen = set()
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


if __name__ == "__main__":
    items = input("Enter words separated by spaces: ").split()
    print(unique_items(items))
