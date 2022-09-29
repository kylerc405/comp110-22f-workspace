"""EX05 - List Utility Tester."""
__author__ = "730564343"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests an empty list returning evens."""
    nums: list[int] = []
    assert only_evens(nums) == []


def test_only_evens_use1() -> None:
    """Tests a normal use case of returning evens."""
    nums: list[int] = [0,1,2,3,4]
    assert only_evens(nums) == [0,2,4]


def test_only_evens_use2() -> None:
    """Tests another normal use case of returning evens."""
    nums: list[int] = [0,1,2,3,6]
    assert only_evens(nums) == [0,2,6]


def test_concat_empty() -> None:
    """Tests 2 empty lists being concatenated."""
    nums1: list[int] = []
    nums2: list[int] = []
    assert concat(nums1, nums2) == []


def test_concat_use1() -> None:
    """Tests 2 normal lists being concatenated."""
    nums1: list[int] = [1,7,5,3]
    nums2: list[int] = [2,5]
    assert concat(nums1, nums2) == [1,7,5,3,2,5]


def test_concat_use2() -> None:
    """Tests 2 normal lists being concatenated."""
    nums1: list[int] = [1,6,4]
    nums2: list[int] = [2]
    assert concat(nums1, nums2) == [1,6,4,2]



def test_sub_empty() -> None:
    """Tests an empty list being returned in the indices specified."""
    nums: list[int] = []
    start: int = 5
    end: int = 10
    assert sub(nums, start, end) == []


def test_sub_use1() -> None:
    """Tests a list being returned in the indices specified."""
    nums: list[int] = [2,7,3,4,7,6]
    start: int = 2
    end: int = 4
    assert sub(nums, start, end) == [3,4]

def test_sub_use2() -> None:
    """Tests a list being returned in the indices specified."""
    nums: list[int] = [2,6,3]
    start: int = 0
    end: int = 1
    assert sub(nums, start, end) == [2]