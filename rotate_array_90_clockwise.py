"""
Actual array is
[
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]

Output should be
[[5, 4, 3, 2, 1],
 [5, 4, 3, 2, 1],
 [9, 8, 7, 6, 5],
 [3, 2, 1, 0, 9],
 [3, 2, 1, 0, 9]]
"""

def rotate_clocwise(arr):
    n = len(arr)
    rotate_matrix = [[] for _ in range(n)]

    for i in reversed(range(n)):
        for j in range(n):
            row = rotate_matrix[j]
            entry = arr[i][j]
            row.append(entry)

    return rotate_matrix

arr = [
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]
rotated_matix = rotate_clocwise(arr)
print(rotated_matix)