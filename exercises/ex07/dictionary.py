"""Practicing dicitonary functions."""

__author__ = "730481986"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Flips values of a dictionary so that keys become values and values become keys."""
    result: dict[str, str] = {}
    new_key_list: list[str] = []
    old_key_list: list[str] = []
    x: int = 0
    check_idx: int = 0
    for key in dictionary:
        new_key_list.append(dictionary[key])
        old_key_list.append(key)
    while x < len(new_key_list):
        while check_idx < len(new_key_list):
            if x != check_idx:
                if new_key_list[x] == new_key_list[check_idx]:
                    raise KeyError(f"Key {new_key_list[x]} was found more than once. ")
            check_idx += 1
        result[new_key_list[x]] = old_key_list[x]
        x += 1
    return result


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the most common favorite color."""
    list_of_fav_colors: list[str] = []
    idx: int = 0
    check_idx: int = 0
    tally: dict[str, int] = {}
    best: int = 0
    best_color: str = ""
    for key in names_and_colors:
        list_of_fav_colors.append(names_and_colors[key])
    while idx < len(list_of_fav_colors):
        if list_of_fav_colors[idx] not in tally:
            tally[list_of_fav_colors[idx]] = 1
            check_idx = 0
            while check_idx < len(list_of_fav_colors):
                if list_of_fav_colors[idx] == list_of_fav_colors[check_idx]: 
                    tally[list_of_fav_colors[idx]] += 1 
                check_idx += 1
        idx += 1
    for key in tally:
        if tally[key] > best:
            best = tally[key]
            best_color = key
    return best_color


def count(list1: list[str]) -> dict[str, int]:
    """Returns how many times a number is found in a list."""
    new_dict: dict[str, int] = {}
    for item in list1:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict

                    

        


        
