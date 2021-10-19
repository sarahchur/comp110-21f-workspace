"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730228276"

from exercises.ex06.dictionaries import invert


def test_invert1() -> None:
    """Test with one key value."""
    x: dict[str, str] = {'a': 'b'}
    assert invert(x) == {'b': 'a'}


def test_invert2() -> None:
    """Test with words."""
    x: dict[str, str] = {'cat': 'dog', 'horse': 'cow'}
    assert invert(x) == {'dog': 'cat', 'cow': 'horse'}


def test_invert3() -> None:
    """Test with names."""
    x: dict[str, str] = {'Sarah': 'Haynes', 'Cat': 'Tristan'}
    assert invert(x) == {'Haynes': 'Sarah', 'Tristan': 'Cat'}

