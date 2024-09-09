from functions import *

def multiplicacion_optimizada(A, B):
    if len(A[0]) != len(B):
        return("No se pueden multiplicar las matrices")

    filas_A = len(A)
    columnas_B = len(B[0])
    C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    bloque_size = 64

    for i in range(0, filas_A, bloque_size):
        for j in range(0, columnas_B, bloque_size):
            for k in range(0, len(B), bloque_size):
                for ii in range(i, min(i + bloque_size, filas_A)):
                    for jj in range(j, min(j + bloque_size, columnas_B)):
                        for kk in range(k, min(k + bloque_size, len(B))):
                            C[ii][jj] += int(A[ii][kk]) * int(B[kk][jj])

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
    C = multiplicacion_optimizada(A, B)
    print('Matriz resultante:', C)
    print('---------------------------------')
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    caso += 1