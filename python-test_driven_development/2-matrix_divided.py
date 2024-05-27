#!/usr/bin/python3
"""This module represent division of matrix with specific number"""


def matrix_divided(matrix, div):
    """Division all elements of a matrix.

       Return:
          A new matrix contains elements after dividing by div

       Possible Errors:
          TypeError and ZeroDivisionError

    """
    matrixError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrixError)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrixError)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(matrixError)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [list(map(lambda i: round(i / div, 2), row)) for row in matrix]
    return result
