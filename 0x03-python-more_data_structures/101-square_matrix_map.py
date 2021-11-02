#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda j: map(lambda i : i**2, matrix[j]), matrix))

#return [[j**2 for j in i] for i in matrix]
