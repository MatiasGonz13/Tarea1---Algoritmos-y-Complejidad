from functions import *
import numpy as np
import math

def remove_zeros(matrix):
    last_row = np.max(np.nonzero(matrix)[0])
    last_col = np.max(np.nonzero(matrix)[1])
    
    new_matrix = matrix[:last_row+1, :last_col+1]
    
    return new_matrix

def resize_matrix(matrix, x):
    new_rows = (2 ** x)
    new_cols = (2 ** x)
    
    new_matrix = np.zeros((new_rows, new_cols))
    
    new_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix
    
    return new_matrix

def strassen(A, B):

    if math.log2(len(A)) - int(math.log2(len(A))) != 0:
        A = resize_matrix(A, math.ceil(math.log2(len(A))))

    elif math.log2(len(A[0])) - int(math.log2(len(A[0]))) != 0:
        A = resize_matrix(A, math.ceil(math.log2(len(A[0]))))

    if math.log2(len(B)) - int(math.log2(len(B))) != 0:
        B = resize_matrix(B, math.ceil(math.log2(len(B))))

    elif math.log2(len(B[0])) - int(math.log2(len(B[0]))) != 0:
        B = resize_matrix(B, math.ceil(math.log2(len(B[0]))))

    n = A.shape[0]

    if n == 1:
        return A * B

    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

fichero = open('Matrices/dataset-matrices.in')
linea1 = fichero.readline()
linea2 = fichero.readline()
caso = 1
while linea1 != "" or linea2 != "":
    print('CASO', caso)
    A = np.array(StrToInt(InputToMatriz(linea1)))
    B = np.array(StrToInt(InputToMatriz(linea2)))
    print('Multiplicacion de las siguientes matrices:')
    print(A)
    print()
    print(B)
    C = strassen(np.array(A), np.array(B))
    C = remove_zeros(C)
    print('Matriz resultante:')
    print(np.array(C))
    print('---------------------------------')
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    caso += 1
    