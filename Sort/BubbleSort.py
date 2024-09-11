import functions
from functions import *

def bubble_sort(lista):
    i = 0
    for i in range(len(lista)):
        j = 0
        for j  in range(len(lista) - 1):
            if (lista[j] > lista[j + 1]):
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp
            j+=1
        i+=1
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
        #print('Lista desordenada:', lista)
        lista = bubble_sort(lista)
        #print('Lista ordenada:', lista)
        linea = fichero.readline()
        caso += 1
        end_time = time.time()
        execution_time = end_time - start_time
        lista_promedio.append(execution_time)
    tiempos_exec.append(cal_average(lista_promedio))
    tamaño_de_muestra.append(len(lista))
    lista_promedio = []

print('DONE')

print(tamaño_de_muestra)
print(tiempos_exec)