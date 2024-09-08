import functions
from functions import *

def division(linea):
    if len(linea) <= 1:
        return linea

    mid = len(linea) //2
    left = linea[:mid]
    right = linea[mid:]

    sortL=division(left)
    sortR=division(right)

    return merge(sortL, sortR)

def merge(left, right):
    lista = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lista.append(left[i])
            i += 1
        else:
            lista.append(right[j])
            j += 1

    lista.extend(left[i:])
    lista.extend(right[j:])

    return lista


fichero = open('dataset-sort.in')
linea = fichero.readline()
caso = 1
while linea != "":
    print('CASO', caso)
    lista = linea[:len(linea)-1].split(',')
    lista = StrToInt(lista)
    print('Lista desordenada:', lista)
    lista = division(lista)
    print('Lista ordenada:', lista)
    print('---------------------------------')
    linea = fichero.readline()
    caso += 1