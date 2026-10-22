"""Task: Decide the winner of a rock-paper-scissors round."""


def winner(first: str, second: str) -> str:
    choices = {"rock", "paper", "scissors"}
    first, second = first.casefold(), second.casefold()
    if first not in choices or second not in choices:
        raise ValueError("choices must be rock, paper, or scissors")
    if first == second:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "first" if beats[first] == second else "second"


if __name__ == "__main__":
    first = input("Player 1 (rock, paper, scissors): ")
    second = input("Player 2 (rock, paper, scissors): ")
    result = winner(first, second)
    print("It's a tie!" if result == "tie" else f"{result.title()} player wins!")
