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


fichero = open('Sort/dataset-sort.in')
linea = fichero.readline()
caso = 1

tamaño_de_muestra = []
lista_promedio = []
tiempos_exec = []

while linea != "":
    for _ in range(10):
        start_time = time.time()
        lista = linea[:len(linea)-1].split(',')
        lista = StrToInt(lista)
        lista = division(lista)
        linea = fichero.readline()
        caso += 1
        end_time = time.time()
        execution_time = end_time - start_time
        lista_promedio.append(execution_time)
    tiempos_exec.append(cal_average(lista_promedio))
    tamaño_de_muestra.append(len(lista))
    lista_promedio = []

print('DONE')

print(tiempos_exec)