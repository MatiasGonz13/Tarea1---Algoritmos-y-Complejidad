from functions import *

def multiplicacion(A, B):
    x1, y1, x2, y2, result = 0, 0, 0, 0, 0

    fila = []
    matriz = []
    
    for _ in range(len(A)):
        for x2 in range(len(B[0])):
            for y2 in range(len(B)):
                result += int(A[y1][x1])*int(B[y2][x2])
                y2+=1
                x1+=1
            fila.append(result)
            result, x1, y2 = 0, 0, 0
            x2 += 1
        matriz.append(fila)
        fila = []
        x1, x2, y2 = 0, 0, 0
        y1 += 1

        return matriz


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
        C = multiplicacion(A, B)
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