"""Recreating the commonly used python functions all, max, and is_equal."""

__author__ = "730481986"


def all(int_list: list[int], single_int: int) -> bool:
    """Returns true if the single integer is found within the list and false if it is not."""
    list_length: int = len(int_list)
    idx: int = 0
    if (list_length == 0):
        return False
    while idx < list_length:
        if (single_int == int_list[idx]):
            idx += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Returns the largest number in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    list_length: int = len(int_list)
    idx: int = 0
    current_max: int = int_list[idx]
    while idx < list_length:
        if int_list[idx] > current_max:
            current_max = int_list[idx]
            idx += 1
        else:
            idx += 1
    return current_max


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Returns if two lists are exactly equal."""
    if len(int_list1) != len(int_list2):
        return False
    idx: int = 0
    while idx < len(int_list1):
        if int_list1[idx] == int_list2[idx]:
            idx += 1
        else:
            return False
    return True