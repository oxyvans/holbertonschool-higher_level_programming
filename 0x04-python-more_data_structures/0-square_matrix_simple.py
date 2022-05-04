#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = matrix.copy()
    for i in range(len(matrix)):
        res[i] = list(map(lambda x: x*x, matrix[i]))
    return(res)
