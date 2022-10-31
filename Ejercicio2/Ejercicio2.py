import random

#Creamos una funcion para crear la matriz

def matriz():
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            n = random.randint(-50, 50)
            matriz[i].append(n)
    return matriz

#Creamos una funcion para resolver el determinante

def determinante(matriz):
    for i in range(len(matriz) * 2):
        if i == 0:
            dp = matriz[0][0] * matriz[1][1] * matriz[2][2] #Calculamos la diagonal principal
        elif i == 1:
            ds = matriz[0][2] * matriz[1][1] * matriz[2][0] #Calculamos la diagonal secundaria
        elif i == 2:
            s1 = matriz[0][1] * matriz[1][2] * matriz[2][0]
        elif i == 3:
            s2 = matriz[1][0] * matriz[2][1] * matriz[0][2]
        elif i == 4:
            r1 = matriz[1][2] * matriz[2][1] * matriz[0][0]
        else:
            r2 = matriz[0][1] * matriz[1][0] * matriz[2][2]
    
    suma = dp + s1 + s2
    resta = ds + r1 +r2
    det = suma - resta
        
    return det


            


    
