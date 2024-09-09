import functions
from functions import *

def bubble_sort(lista):
    j=0
    while j < len(lista)-1:
        i = 0
        while i < len(lista)-1:
            if int(lista[i]) > int(lista[i+1]):
                lista = swap(lista[i], lista[i+1], lista)
            i+=1
        j+=1
    return(lista)

fichero = open('Sort/dataset-sort.in')
linea = fichero.readline()
caso = 1

while linea != "":
    print('CASO', caso)
    lista = linea[:len(linea)-1].split(',')
    lista = StrToInt(lista)
    print('Lista desordenada:', lista)
    lista = bubble_sort(lista)
    print('Lista ordenada:', lista)
    print('---------------------------------')
    linea = fichero.readline()
    caso += 1
    