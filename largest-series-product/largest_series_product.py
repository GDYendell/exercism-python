import re
from functools import reduce


def largest_product(series: str, size: int):
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif re.match("^[0-9]+$", series) is None:
        raise ValueError("digits input must only contain digits")

    digits = tuple(int(d) for d in series)
    largest = 0
    for idx in range(len(digits) - size + 1):
        window_sum = reduce(lambda x, y: x * y, digits[idx : idx + size])
        if window_sum > largest:
            largest = window_sum

    return largest
