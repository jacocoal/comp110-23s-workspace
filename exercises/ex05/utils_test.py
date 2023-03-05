"""Performing unit tests on the utils file."""

__author__ = "730481986"

from exercises.ex05.utils import only_evens, sub, concat

def test_evens() -> None:
    test_list: list[int] = [2, 3, 4, 8]
    assert only_evens(test_list) == [2, 4, 8]

def test_with_negatives() -> None:
    test_list: list[int] = [-4, -2, -1, 0]
    assert only_evens(test_list) == [-4, -2, 0]

def test_empty() -> None:
    test_list: list[int] = list()
    assert only_evens(test_list) == []

def test_many_indexes() -> None:
    test_list: list[int] = [0, 1, 2, 3, 4, 5, 6]
    test_start: int = 0
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [0, 1, 2, 3]

def test_negative() -> None:
    test_list: list[int] = [-1, -2, -3, 4]
    test_start: int = 1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [-2, -3, 4]

def test_wrong_idx() -> None:
    test_list: list[int] = [1, 2, 3]
    test_start: int = 1
    test_end: int = 0
    assert sub(test_list, test_start, test_end) == []

def test_many() -> None:
    test_list1: list[int] = [0, 1, 2]
    test_list2: list[int] = [0, 2, 2]
    assert concat(test_list1, test_list2) == [0, 1, 2, 0, 2, 2]

def test_negative_lists() -> None:
    test_list1: list[int] = [-2, 0, 1]
    test_list2: list[int] = [-1, 0]
    assert concat(test_list1, test_list2) == [-2, 0, 1, -1, 0]

def test_one_empty_list() -> None:
    test_list1: list[int] = [22, 1]
    test_list2: list[int] = list()
    assert concat(test_list1, test_list2) == [22, 1]