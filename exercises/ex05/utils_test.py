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


def test_sub1() -> None:
    """Test sub to include only numbers specified by indicies."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub2() -> None:
    """Test sub for a long list of numbers."""
    a_list: list[int] = [30, 40, 20, 10, 5, 8, 10, 20, 50, 20, 60]
    assert sub(a_list, 2, 8) == [20, 10, 5, 8, 10, 20] 


def test_sub3() -> None:
    """Test sub for an index of 0."""
    a_list: list[int] = [1, 2, 3, 5, 6, 6, 7]
    assert sub(a_list, 0, 5) == [1, 2, 3, 5, 6]


def concat1() -> None:
    """Test concat for the same length and numbers."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [1, 2, 3]
    assert concat(x, y) == [1, 2, 3, 1, 2, 3]