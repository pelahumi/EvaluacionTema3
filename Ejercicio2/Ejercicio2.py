import random

#Creamos una funcion para crear la matriz

def matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            n = random.randint(0,100)
            matriz[i].append(n)
    return matriz

#Creamos una funcion para resolver el determinante

def determinante(matriz):
    for i in range(len(matriz)):
        dp = dp + matriz[i][i]

    j = -1
    for i in range(len(matriz)):
        dp2 = dp2 + matriz[i][j]
    
    

    

    
            


    
