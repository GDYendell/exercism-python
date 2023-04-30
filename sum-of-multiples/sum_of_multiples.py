from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    return sum(
        set(
            value
            for multiple in multiples if multiple > 0
            for value in range(multiple, limit, multiple)
        )
    )
