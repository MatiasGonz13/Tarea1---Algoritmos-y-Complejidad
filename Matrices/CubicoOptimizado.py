from functions import *

def multiplicacion_optimizada(A, B):

    n = len(A)
    m = len(A[0])
    p = len(B[0])
    
    B_T = [[B[j][i] for j in range(m)] for i in range(p)] # matriz B transpuesta
    
    C = [[0 for _ in range(p)] for _ in range(n)]
    
    for i in range(n):
        for j in range(p):
            C[i][j] = sum(A[i][k] * B_T[j][k] for k in range(m))
    
    return C


fichero = open('Matrices/dataset-matrices-cuadradas.in')
linea1 = fichero.readline()
linea2 = fichero.readline()
caso = 1

tamaño_de_muestra = []
lista_promedio = []
tiempos_exec = []

while linea1 != "":
    for _ in range(1):
        start_time = time.time()
        A = np.array(StrToInt(InputToMatriz(linea1)))
        B = np.array(StrToInt(InputToMatriz(linea2)))
        C = multiplicacion_optimizada(A, B)
        linea1 = fichero.readline()
        linea2 = fichero.readline()
        caso += 1
        end_time = time.time()
        execution_time = end_time - start_time
        lista_promedio.append(execution_time)
    tiempos_exec.append(cal_average(lista_promedio))
    tamaño_de_muestra.append(len(A))
    lista_promedio = []
    print('A')

print('DONE')

print(tiempos_exec)