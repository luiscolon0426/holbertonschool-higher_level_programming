#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        new_matrix = [[i*i for i in j] for j in matrix]
    return new_matrix
