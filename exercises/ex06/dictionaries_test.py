"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730228276"

from exercises.ex06.dictionaries import invert


def test_invert() -> None:
    """Test with one key and one value in dictionary."""
    x: dict[str, str] = {'a': 'b'}
    assert invert(x) == {'b': 'a'}










# def test_invert1() -> None: 
#     """Invert a dictionary with one key."""
#     x: dict[str, str] = {'a': 'b'}
#     assert invert(x) == {'b': 'a'}


# def test_invert2() -> None:
#     """Invert a dictionary with three keys."""
#     x: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
#     assert invert(x) == {'b': 'a', 'd': 'c', 'f': 'e'}


# def test_invert() -> None:
#     """Invert a dictioary with names."""
#     x: dict[str, str] = {'Sarah': 'Haynes'}
#     assert invert(x) == {'Haynes': 'Sarah'}