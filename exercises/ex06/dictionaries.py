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
    colors_numbers: dict[str, int] = {}
    for key in x: 
        color = x[key]
        if color not in colors_numbers:
            colors_numbers[color] = 1
        else:
            colors_numbers[color] += 1 
    for key in colors_numbers:
        number = colors_numbers[key]
        if number in colors_numbers > colors_numbers:
            return key

        





# def count(x: list[str]) -> dict[str,int]:
#     """Count # of times value appeared."""
#     result = {}
#     for key in result:
        
