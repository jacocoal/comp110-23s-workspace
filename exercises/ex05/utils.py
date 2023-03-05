"""Implementing funtion skeletons and implementations."""

__author__ = "730481986"


def only_evens(int_list: list[int]) -> list[int]:
    """Returns the even numbers in a list of integers."""
    evens_list: list[int] = list()
    for item in int_list:
        if item % 2 == 0:
            evens_list.append(item)
    return evens_list


def concat(int_list1: list[int], int_list2: list[int]) -> list[int]:
    """Returns a combination of the first list followed by the second list."""
    comb_list: list[int] = list()
    for item1 in int_list1:
        comb_list.append(item1)
    for item2 in int_list2:
        comb_list.append(item2)
    return comb_list


def sub(int_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a subset of the given list that falls between the start index and the end index. """
    sub_list: list[int] = list()
    if start_idx < 0:
        start_idx == 0
    if end_idx > len(int_list):
        end_idx == (len(int_list) - 1)
    if len(int_list) == 0 or start_idx >= len(int_list) or end_idx <= 0:
        return []
    for idx in range(start_idx, end_idx + 1):
        sub_list.append(int_list[idx])
    return sub_list

        