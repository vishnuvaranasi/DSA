# Objective
from unittest import result


# Get comfortable with nested loops and accessing elements in 2D arrays.
# Practice traversal, element-wise conditions, and simple aggregations.

# 1. Transpose a Matrix
# 2. Sum of Diagonals in a Square Matrix
# 3. Find All Zeros in a 2D Array

def tranpose_matrix(matrix):
    r = len(matrix)
    if r == 0:
        return matrix
    c = len(matrix[0])
    result = [[0] * r for i in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][i] = matrix[i][j]
    return result

print(tranpose_matrix([[1, 2, 3], [4, 5, 6]]))
print(tranpose_matrix([[7, 8]]))

# Edge cases: empty matrix : empty matrix is returned
# Time complexity: O(r * c) as parsing includes all elements in rows and columns
# Space complexity: O(r * c) as the return matrix occupies space for storing all elements

def sum_diagonals(matrix):
    result = 0
    r = len(matrix)
    if r == 0:
        return 0

    c = len(matrix[0])
    if r != c:
        return None

    for i in range(r):
        result += matrix[i][i]

    c = 0
    for i in range(r-1,-1,-1):
        if i != c:
            result += matrix[i][c]
        c += 1

    return result

print(sum_diagonals([[1,2,3], [4,5,6], [7,8,9]]))
print(sum_diagonals([[5,1], [2,6]]))

# Edge cases: zero in case of an empty matrix, None in case of a non-square matrix
# Time complexity: O(n) as parsing includes all elements in diagonals
# Space complexity: O(1) as only sum of diagonals need to be stored

def get_zero_locations(matrix):
    result = []
    r = len(matrix)
    if r == 0:
        return result
    c = len(matrix[0])

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                result.append([i,j])

    return result

print(get_zero_locations([[1,0], [0,1]]))
print(get_zero_locations([[1,2], [3,4]]))

# Edge cases: in case of an empty matrix, empty result shall be returned
# Time complexity: O(r * c) as parsing includes all elements in matrix
# Space complexity: O(r * c) as locations of zeros need to be stored to return, worst case of all zeros
