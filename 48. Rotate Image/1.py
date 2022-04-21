from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # each new place for a given position(i,j) can be calculated by the 
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
rotate([[1,2,3],[4,5,6],[7,8,9]])