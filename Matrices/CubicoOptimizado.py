from functions import *

def multiplicacion_optimizada(A, B):
    if len(A[0]) != len(B):
        return "Las matrices no son compatibles para la multiplicación"
    # Suponemos que A es de tamaño n x m y B es de tamaño m x p
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    
    # Transponer la matriz B para mejorar la localidad de los datos
    B_T = [[B[j][i] for j in range(m)] for i in range(p)]
    
    # Inicializar la matriz C de tamaño n x p con ceros
    C = [[0 for _ in range(p)] for _ in range(n)]
    
    # Multiplicar A con la matriz transpuesta de B
    for i in range(n):
        for j in range(p):
            # Producto escalar de la fila i de A y la fila j de B^T (que es la columna j de B)
            C[i][j] = sum(A[i][k] * B_T[j][k] for k in range(m))
    
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
    print('Matriz resultante:')
    print(np.array(C))
    print('---------------------------------')
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    caso += 1
    