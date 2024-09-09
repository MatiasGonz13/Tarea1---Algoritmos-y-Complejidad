from functions import *
import numpy as np

def strassen(A, B):
    # Comprueba si las matrices son cuadradas
    if A.shape != B.shape:
        return("Las matrices deben ser de tamaño 2^x")
    n = A.shape[0]

    # Caso base: matrices de tamaño 1x1
    if n == 1:
        return A * B

    # Paso 1: Dividir las matrices
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Paso 2: Calcular las siete multiplicaciones
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Paso 3: Combinar los resultados
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combinar las submatrices
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
    print('Matriz resultante:')
    print(C)
    print('---------------------------------')
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    caso += 1
    