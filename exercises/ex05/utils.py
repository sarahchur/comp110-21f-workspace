"""List utility functions part 2."""

__author__ = "730228276"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """Return only even numbers from the list we entered."""
    i: int = 0
    evens: list[int] = list()
    while i < len(x):
        if x[i] % 2 == 0:
            evens.append(x[i])
        i += 1
    return evens


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Return a subset of a_list between the 2 values."""
    i: int = 0
    subset: list[int] = list()
    while i < len(a_list):
        if x == a_list[i]:
            subset.append(x[i])
        i += 1
        

    



    





