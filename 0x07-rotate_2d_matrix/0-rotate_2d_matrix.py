#!/usr/bin/python3
"""
Rotate 2D Matrix func
"""


def rotate_2d_matrix(matrix):
    """this func rotates two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    num = len(matrix)
    for i in range(int(num / 2)):
        y = (num - i - 1)
        for j in range(i, y):
            x = (num - 1 - j)
            # current number
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[x][i]
            # change left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp
