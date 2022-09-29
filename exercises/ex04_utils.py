"""EX04 - Lists."""
__author__ = "730564343"


def all(list: list[int], num: int) -> bool:
    """Returns true if each number in the list matches the given number."""
    if len(list) == 0:
        return False
    i: int = 0
    while i < len(list):
        if list[i] != num: 
            return False

        i += 1

    return True


def max(list: list[int]) -> int:
    """Returns the maximum value in the list of ints."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    max: int = list[0]
    while i < len(list) - 1:
        if list[i + 1] > max:
            max = list[i + 1]

        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true if the 2 lists are identical in values at each index."""
    i: int = 0
    if len(list1) == len(list2):
        while i < len(list1):
            if list1[i] != list2[i]:
                return False

            i += 1 
    else:
        return False

    return True