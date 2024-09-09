import numpy as np

def InputToMatriz(linea):
    matriz = []
    string = linea[:len(linea)-1].split(';')
    for i in string:
        matriz.append(i.split(','))
    return matriz

def StrToInt(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz