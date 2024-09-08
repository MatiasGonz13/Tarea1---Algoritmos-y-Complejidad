import functions
from functions import *

fichero = open('dataset-sort.in')
linea = fichero.readline()
caso = 1
while linea != "":
    lista = linea[:len(linea)-1].split(',')
    lista = StrToInt(lista)
    print('Lista desordenada:', lista)
    lista.sort()
    print('Lista ordenada:', lista)
    print('---------------------------------')
    linea = fichero.readline()
    caso += 1