#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [list(map(lambda i: round(i / div, 2), row)) for row in matrix]
    return result
