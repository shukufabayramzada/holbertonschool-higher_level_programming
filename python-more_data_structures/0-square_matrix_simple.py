#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    result = [list(map(lambda i: i ** 2, row)) for row in new_matrix]
    return result
