#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        print(" ".join("{:d}".format(x) for x in ele))
