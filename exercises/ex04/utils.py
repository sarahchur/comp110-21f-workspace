"""List utility functions."""

__author__ = "730228276"


def all(x: list[int], y: int) -> bool:
    """Return boolean values when comparing an integer to my list."""
    i: int = 0
    while i < len(x):
        if y == x[i]:
            return True
        i = i + 1
    return False
