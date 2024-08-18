import functions
from functions import *

fichero = open('dataset-sort.txt')
linea = fichero.readline()

while linea != "":
    lista = linea[:len(linea)-1].split(',')
    print('Lista desordenada:', lista)
    j=0
    while j < len(lista)-1:
        i = 0
        while i < len(lista)-1:
            if int(lista[i]) > int(lista[i+1]):
                lista = swap(lista[i], lista[i+1], lista)
            i+=1
        j+=1
    print('Lista ordenada:', lista)
    print('---------------------------------')
    linea = fichero.readline()