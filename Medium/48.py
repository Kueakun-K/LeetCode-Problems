from typing import List
def rotate(matrix: List[List[int]]) -> None:
    newMatrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[j][i])
        newMatrix.append(temp)
    matrix = newMatrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))