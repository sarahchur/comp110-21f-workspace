"""Practice with dictionaries."""

__author__ = "730228276"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert keys and values."""
    invert_x: dict[str, str] = {}
    for key in x:
        y: str = x[key]
        if y in invert_x:
            raise KeyError("Duplicate key found!")
        invert_x[y] = key
    return invert_x
        

def favorite_color(x: dict[str, str]) -> str:
    """Return a str of color that appeared most."""


def count(x: list[str]) -> dict[str,int]:
    """Count # of times value appeared."""
    result = {}
    for key in result:
        
