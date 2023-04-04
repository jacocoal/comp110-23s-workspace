"""We out hear wranglin' some data."""

__author__ = "730481986"


DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers"""
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column vales
        result[key] = column_values(table, key)
    return result


def head(dict1: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    head_dict: dict[str, list[str]] = {}
    for key in dict1:
        head_list: list[str] = []
        idx: int = 0
        if number_of_rows <= len(dict1.keys()):
            while idx < number_of_rows:
                head_list.append(dict1[key][idx])
                idx += 1
            head_dict[key] = head_list
        else:
            head_dict = {}
    return head_dict


def select(dict1: dict[str, list[str]], list1: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    select_dict: dict[str, list[str]] = {}
    idx: int = 0
    while idx < len(list1):
        select_dict[list1[idx]] = dict1[list1[idx]]
        idx += 1
    return select_dict


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    concat_dict: dict[str, list[str]] = {}
    for key in dict1:
        concat_dict[key] = dict1[key]
    for key in dict2:
        if key in concat_dict:
            concat_dict[key] = concat_dict[key] + dict2[key]
        else:
            concat_dict[key] = dict2[key]
    return concat_dict


def count(list1: list[str]) -> dict[str, int]:
    """Returns how many times a number is found in a list."""
    new_dict: dict[str, int] = {}
    for item in list1:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict