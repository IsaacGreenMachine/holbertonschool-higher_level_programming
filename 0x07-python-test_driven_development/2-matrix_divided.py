#!/usr/bin/python3
"""This is the module for a matrix division function."""


def matrix_divided(matrix, div):
    """This divides all numbers in a matrix by div."""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    if size == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    newMatrix = []
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        newMatrix.append([])
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [float, int]:
                raise TypeError("""matrix must be a matrix
                (list of lists) of integers/floats""")
            newMatrix[i].append(round(matrix[i][j] / div, 2))
    return newMatrix
