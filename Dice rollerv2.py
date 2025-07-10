import random
from typing import List, Union


def roll(dice: str, n: int = 1) -> Union[int, List[int]]:
    """
    From Chatgpt
    Roll an NdX‑style die string (e.g. 'd6', 'd20').

    Parameters
    ----------
    dice : str
        Die notation starting with 'd' followed by the number of sides.
    n : int, default 1
        How many times to roll the die.

    Returns
    -------
    int | list[int]
        A single integer if n == 1, otherwise a list of integers.
    """
    if not dice.startswith("d") or not dice[1:].isdigit():
        raise ValueError(f"{dice!r} is not of the form 'd<number>'")

    sides = int(dice[1:])  # e.g. 'd8' → 8
    if sides < 2:
        raise ValueError("A die needs at least two sides")

    rolls = [random.randint(1, sides) for _ in range(n)]
    return rolls[0] if n == 1 else rolls


input(roll())