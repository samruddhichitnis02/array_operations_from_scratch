import numpy as np

def fill_mat(row, col):
    mat = []

    for i in range(row):
        rows = []
        for j in range(col):
            ele = int(input('Enter the elements of the matrix - '))
            rows.append(ele)
        mat.append(rows)
    return mat

row = int(input('Enter the number of rows for 1st array- '))
col = int(input('Enter the number of columns for 2nd array- '))

mat = fill_mat(row, col)
print(mat)