import numpy as np
import time
import matplotlib.pyplot as plt

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

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    avg = sum_num / len(num)
    return avg