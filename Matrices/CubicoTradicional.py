from functions import *

def multiplicacion(A, B):
    if len(A[0]) != len(B):
        return "Las matrices no son compatibles para la multiplicación"
    else:
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        result = 0
        fila = []
        matriz = []
        for _ in range(len(A)):
            for x2 in range(len(B[0])):
                for y2 in range(len(B)):
                    result += int(A[y1][x1])*int(B[y2][x2])
                    y2+=1
                    x1+=1
                fila.append(result)
                result=0
                x1 = 0
                x2 += 1
                y2 = 0
            matriz.append(fila)
            fila = []
            x1 = 0
            y1 += 1
            x2 = 0
            y2 = 0

        return matriz


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
    C = multiplicacion(A, B)
    print('Matriz resultante:', C)
    print('---------------------------------')
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    caso += 1
