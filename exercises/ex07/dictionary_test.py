"""EX07 - Dictionary Function Tester"""
__author__ = "730564343"

from exercises.ex07.dictionary import invert, favorite_color, count

def test_invert_edge() -> None:
    """Invert dictionary of zero length."""
    orig: dict[str, str] = {}
    assert invert(orig) == {}


def test_invert_use1() -> None:
    """Testing inverse function use case 1."""
    orig: dict[str, str] = {"soup": "night"}
    assert invert(orig) == {"night": "soup"}


def test_invert_use2() -> None:
    """Testing inverse function use case 2."""
    orig: dict[str, str] = {"hello": "friend", "1": "2"}
    assert invert(orig) == {"friend": "hello", "2": "1"}


def test_color_edge() -> None:
    """Testing empty color dictionary."""
    orig: dict[str, str] = {}
    assert favorite_color(orig) == ""


def test_color_use1() -> None:
    """Testing color dictionary use case 1."""
    orig: dict[str, str] = {"kyler": "purple", "adam": "green"}
    assert favorite_color(orig) == "purple"


def test_color_use2() -> None:
    """Testing color dictionary use case 1."""
    orig: dict[str, str] = {"kyler": "purple", "adam": "green", "joseph": "green"}
    assert favorite_color(orig) == "green"


def test_count_edge() -> None:
    """Testing empty count list."""
    orig: list[str] = []
    assert count(orig) == {}


def test_count_use1() -> None:
    """Testing count use case 1."""
    orig: list[str] = [1, 2, 3, 4]
    assert count(orig) == {1: 1, 2: 1, 3: 1, 4: 1}


def test_count_use2() -> None:
    """Testing count use case 1."""
    orig: list[str] = [1, 1, 1, 3]
    assert count(orig) == {1: 3, 3: 1}