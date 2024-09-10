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
    