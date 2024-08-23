fichero = open('dataset-sort.txt')
linea = fichero.readline()
while linea != "":
    lista = linea[:len(linea)-1].split(',')
    
    newlista = []
    for i in lista:
        newlista.append(int(i))
    print(newlista)

    linea = fichero.readline()