"""
Actual array is
[
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]

output should be
[[9, 0, 1, 2, 3], 
 [9, 0, 1, 2, 3], 
 [5, 6, 7, 8, 9], 
 [1, 2, 3, 4, 5], 
 [1, 2, 3, 4, 5]]
"""

def rotate_counter_clockwise(arr):
    n = len(arr)
    rotated_arr = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            k = n - j - 1
            row = rotated_arr[k]
            entry = arr[i][j]
            row.append(entry)
    
    return rotated_arr
         
arr = [
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]

rotated_array = rotate_counter_clockwise(arr)   
print(rotated_array)