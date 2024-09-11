import functions
from functions import *

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
        lista.sort()
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