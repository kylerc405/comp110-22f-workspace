"""EX05 - List Utility Functions."""
__author__ = "730564343"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only even numbers in the given list."""
    evens: list[int] = []

    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    return evens


def concat(nums1: list[int], nums2: list[int]) -> list[int]:
    """Returns both lists concatenated into one."""
    combo: list[int] = []

    for n in nums1:
        combo.append(n)

    for n in nums2:
        combo.append(n)
    
    return combo


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns a list that is the subset of the given list from the indexes specified."""
    subbed: list[int] = []

    i: int = start

    if len(nums) == 0 or start >= len(nums) or end <= 0 or start < 0 or end >= len(nums):
        return subbed

    while i < end:
        subbed.append(nums[i])
        i += 1
    
    return subbed