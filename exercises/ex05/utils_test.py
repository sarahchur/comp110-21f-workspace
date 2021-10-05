"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730228276"


def test_only_evens() -> None:
    """Test only_evens to account for only even numbers in the list"""
    x: list[int] = [1, 2, 3, 4]
    assert sum(x) == [2, 4]


def test_sub() -> None:
    """Test sub to include only numbers specified by indicies"""
    a_list: list[int] = [10, 20, 30, 40]
    x: int = 1
    y: int = 3
    assert sum(a_list) == [20, 30]