import functions
from functions import *

def quick_sort(lista, inicio, fin):
    if inicio > fin:
        return
    i = inicio
    j = fin
    pivote = lista[inicio]

    while i < j:
        while i < j and lista[j] > pivote:
            j = j - 1

        if i < j:
            lista[i] = lista[j]
            i = i + 1

        while i < j and lista[i] <= pivote:
            i = i + 1

        if i < j:
            lista[j] = lista[i]
            j = j - 1

        lista[i] = pivote
        
    quick_sort(lista, inicio, i - 1)
    quick_sort(lista, i + 1, fin)

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
        quick_sort(lista, 0, len(lista)-1)
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