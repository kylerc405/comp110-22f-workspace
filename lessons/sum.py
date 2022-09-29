"""Example."""


def sum(xs: list[float]) -> float:
    "Compute sum of list."
    total: float = 0.0
    i: int = 0 
    while i < len(xs):
        total += xs[i]
        i += 1
    return total
