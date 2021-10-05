"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730228276"


from exercises.ex05.utils import only_evens, sub


def test_only_evens1() -> None:
    """Test only_evens to account for increasing numbers in a list."""
    x: list[int] = [1, 2, 3, 4]
    assert only_evens(x) == [2, 4]


def test_only_evens2() -> None:
    """Test only_evens to account for only odds in a lists."""
    x: list[int] = [1, 3, 5, 7]
    assert only_evens(x) == []


def test_only_evens3() -> None:
    """Test only_evens to account for a list of all evens."""
    x: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(x) == [2, 4, 6, 8, 10]


def test_sub() -> None:
    """Test sub to include only numbers specified by indicies."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]