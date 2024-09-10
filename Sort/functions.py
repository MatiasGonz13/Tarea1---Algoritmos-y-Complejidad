import time
import matplotlib.pyplot as plt
'''
Funcion que transforma los elementos de la lista de Sting a Integer
Esto de debio añadir por el tipo de input, sin embargo si el input 
se hace de forma directa con un input(), se puede evitar
'''
def StrToInt(lista):
    newlista = []
    for item in lista:
        newlista.append(int(item))
    return newlista

#Funcion que toma dos elementos de una lista, y los intercambia de lugar
def swap(elemento1, elemento2, lista):
    indice1 = lista.index(elemento1)
    indice2 = lista.index(elemento2)
    lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
    return lista
