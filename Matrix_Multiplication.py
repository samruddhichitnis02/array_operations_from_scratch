import numpy as np 

def create_matrix(rows, cols):
    mat = []
    for i in range(rows):
        rows = []
        for j in range(cols):
            ele = int(input('Enter the elements of the array - '))
            rows.append(ele)
        mat.append(rows)
    mat = np.array(mat)
    return mat


def multiply_matrix(matA, matB):
    # Note : For matrix multiplication the rule is 
    # matA = m x n
    # matB = n x k
    # then matA * matB is possible only if matA.shape[1] = matB.shape[0] that is n = n
    # shape of the resulting matrix is m x k

    if matA.shape[1] == matB.shape[0]:
        res = np.zeros([matA.shape[0], matB.shape[1]])
        
        # number of rows in resultant matrix will be given by below for loop
        for i in range(res.shape[0]):

            # number of columns in resultant matrix will be given by below for loop
            for j in range(res.shape[1]):

                # below for loop is to carry out the multiplication and addition operation
                for k in range(matA.shape[1]):
                    res[i][j] += matA[i][k] * matB[k][j]

        return res

rowA = int(input('Enter the rows of matrix A - '))
colA = int(input('Enter the cols of matrix A - '))

matA = create_matrix(rowA, colA)
print(matA)

rowB = int(input('Enter the rows of matrix B - '))
colB = int(input('Enter the cols of matrix B - '))

matB = create_matrix(rowB, colB)
print(matB)

res = multiply_matrix(matA, matB)
print(res)