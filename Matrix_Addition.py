import numpy as np 

def create_matrix(rows, cols):
    mat = []
    for i in range(rows):
        rows = []
        for j in range(cols):
            ele = int(input('Enter the elements of matrix'))
            rows.append(ele)
        mat.append(rows)
    mat = np.array(mat)

    return mat

def matrix_addition(matA, matB):
    if (matA.shape) == (matB.shape):
        res = np.zeros(matA.shape)

        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res[i][j] = matA[i][j] + matB[i][j]

        return res
    else:
        print('Matrix multiplication cannot be performed as the order of Matrix A and B is not same')

rowsA = int(input('Enter the number of rows of matrix1 - '))
colsA = int(input('Enter the number of cols of matrix1 - '))
matA = create_matrix(rowsA, colsA)
print(matA)

rowsB = int(input('Enter the number of rows of matrix2 - '))
colsB = int(input('Enter the number of cols of matrix2 - '))
matB = create_matrix(rowsB, colsB)
print(matB)

result = matrix_addition(matA, matB)
print(result)