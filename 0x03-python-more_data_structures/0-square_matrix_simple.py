#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[j**2 for j in i] for i in matrix]


'''
return list(map(squaredArray, matrix))
def squaredArray(arr):
a = []
for i in arr:
a.append(i**2)
return a
'''
