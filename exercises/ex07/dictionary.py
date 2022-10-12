"""EX07 - Dictionary Functions"""
__author__ = "730564343"

def invert(orig: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values."""
    inv: dict[str, str] = dict()

    for key in orig:
        if orig[key] in inv:
            raise KeyError("Duplicate keys found!")
        inv[orig[key]] = key

    return inv


def favorite_color(orig: dict[str, str]) -> str:
    """Returns the most frequent favorite color."""

    colors: list[str] = list()
    count: list[int] = []
    i: int = 0
    max: int = 0

    if orig == {}:
        return ""

    for key in orig:
        if orig[key] not in colors:
            colors.append(orig[key])
            count.append(1)
            i += 1
        else:
            index: int = colors.index(orig[key])
            count[index] += 1
    
    j: int = len(count)-1

    while j > 0:
        if count[j] > count[j-1]:
            max = j
        j -= 1

    return colors[max]


def count(list: list[str]) -> dict[str, int]:
    """Returns a dictionary with keys of list values, and the values being the frequency of each list value."""
    freq: dict[str, int] = dict()

    for item in list:
        if item not in freq:
            freq[item] = 1
        else:
            freq[item] += 1

    return freq


print(count([1,2,3,4]))