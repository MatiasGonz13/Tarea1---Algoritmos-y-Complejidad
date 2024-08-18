#Funcion que toma dos elementos de una lista, y los intercambia de lugar
def swap(elemento1, elemento2, lista):
    indice1 = lista.index(elemento1)
    indice2 = lista.index(elemento2)
    lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
    return lista
