"""Unit tests for the dictionary file."""

__author__ = "730481986"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_regular_invert() -> None:
    """Tests the invert funtion to make sure a multitude of entries returns the correct result."""
    test_many_dict: dict[str, str] = {'hair': 'red', 'shirt': 'blue', 'pants': 'brown'}
    assert invert(test_many_dict) == {'red': 'hair', 'blue': 'shirt', 'brown': 'pants'}


def test_many_invert() -> None:
    """Tests the invert function to make sure more than 5 entries returns the correct amount."""
    test_integers_dict: dict[str, str] = {"cold": "steel", "big": "chungus", "Marty": "McFly", "Johnny": "Knoxville", "Bradley": "Nowell"}
    assert invert(test_integers_dict) == {"steel": "cold", "chungus": "big", "McFly": "Marty", "Knoxville": "Johnny", "Nowell": "Bradley"}


def test_empty_invert() -> None:
    """Tests the invert function to make sure an empty dictionary returns and empty list."""
    test_empty_dict: dict[str, str] = {}
    assert invert(test_empty_dict) == {}


def test_favorite_color() -> None:
    """Tests to make sure the correct favorite color is returned in a list."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_more_than_two() -> None:
    """Tests to make sure that the color that is listed on the dictionary first is returned when there is a tie for favorite color."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(colors) == "yellow"


def test_empty_colors() -> None:
    """Tests to return nothing when the dictionary is empty."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_regular() -> None:
    """Tests to ensure count works properly given regular inputs."""
    list1: list[str] = ["dog", "cat", "dog", "bird"]
    assert count(list1) == {"dog": 2, "cat": 1, "bird": 1}


def test_large() -> None:
    """Tests to ensure count works properly given more than 5 inputs."""
    list1: list[str] = ["dog", "cat", "dog", "bird", "llama", "cat", "dog"]
    assert count(list1) == {"dog": 3, "cat": 2, "bird": 1, "llama": 1}


def test_empty_count() -> None:
    """Tests to return nothing when the list is empty."""
    list1: list[str] = []
    assert count(list1) == {}