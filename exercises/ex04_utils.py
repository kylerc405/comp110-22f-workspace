"""EX04 - Lists."""
__author__ = "730564343"

def all(list: list[int], num: int) -> bool:
    i: int = 0
    while i < len(list):
        if list[i] != num: 
            return False
        i+=1

    return True

def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    max: int = list[0]
    while i < len(list)-1:
        if list[i+1] > list[i]:
            max = list[i+1]

        i+=1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    if len(list1) == len(list2):
        while i < len(list1):
            if list1[i] != list2[i]:
                return False
            i+=1 
    else:
        return False

    return True