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
    
    s1 = matriz[0][1] * matriz[1][2] * matriz[2][0]
    s2 = matriz[1][0] * matriz[2][1] * matriz[0][2]

    r1= matriz[0][1] * matriz[1][0] * matriz[2][2]
    r2 = matriz[2][1] * matriz[1][2] * matriz[0][0]
 
    detereminante = dp + s1 + s2 - (dp2 + r1 + r2)
    
    return determinante

            


    
