from typing import Dict, List


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    if matrix and len(set(map(len, matrix))) != 1:
        raise ValueError("irregular matrix")

    saddle_points: List[Dict[str, int]] = []
    for idx, row in enumerate(matrix):
        row_peak = max(row)
        row_peak_indexes = [idx for idx, value in enumerate(row) if value == row_peak]
        for row_peak_idx in row_peak_indexes:
            peak_column = [row[row_peak_idx] for row in matrix]
            if min(peak_column) == row_peak:
                saddle_points.append(dict(row=idx + 1, column=row_peak_idx + 1))

    return saddle_points
