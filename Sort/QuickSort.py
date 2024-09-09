import functions
from functions import *

def quick_sort(lista, inicio, fin):
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivote = lista[inicio]

    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivote:
            posterior = posterior - 1

        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior = anterior + 1

        while anterior < posterior and lista[anterior] <= pivote:
            anterior = anterior + 1

        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior = posterior - 1

        lista[anterior] = pivote
        
    quick_sort(lista, inicio, anterior - 1)
    quick_sort(lista, anterior + 1, fin)

fichero = open('Sort/dataset-sort.in')
linea = fichero.readline()
caso = 1
while linea != "":
    print('CASO', caso)
    lista = linea[:len(linea)-1].split(',')
    lista = StrToInt(lista)
    print('Lista desordenada:', lista)
    quick_sort(lista, 0, len(lista)-1)
    print('Lista ordenada:', lista)
    print('---------------------------------')
    linea = fichero.readline()
    caso += 1
    