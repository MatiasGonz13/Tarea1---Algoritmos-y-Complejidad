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

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    avg = sum_num / len(num)
    return avg