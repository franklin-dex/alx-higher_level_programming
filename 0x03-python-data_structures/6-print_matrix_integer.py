#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for e in range(len(matrix[r])):
            print("{:d}".format(matrix[r][e]), end="")
            if e != (len(matrix[r]) - 1):
                print(" ", end="")

        print("")
