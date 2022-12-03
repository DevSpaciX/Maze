from more_itertools import locate


def find_closest_gate(matrix_row: str, value: int, gate: str = ".") -> int:
    matrix_row = list(locate(matrix_row[0], lambda x: x == gate))
    return min(matrix_row, key=lambda x: abs(x - value))
