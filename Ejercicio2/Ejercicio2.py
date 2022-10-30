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
    dp = 1
    ds = 1
    s1 = 1
    s2 = 1
    r1 = 1
    r2 = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                dp = dp * matriz[i][j]
            elif (i - j == -1) or (i - j == 2):
                s1 = s1 * matriz[i][j]
            elif (i - j == 1) or (i - j == -2):
                s2 = s2 * matriz[i][j]
            elif (i - j == 2) or (i==1 and j==1) or (i - j == -2):
                ds = ds * matriz[i][j]
            elif (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 2 and j == 2):
                r1 = r1 * matriz[i][j]
            elif (i == 0 and j == 0) or (i == 1 and j == 2) or (i == 2 and j ==1):
                r2 = r2 * matriz[i][j]
    solucion = dp + s1 + s2 - ds - r1- r2
    return solucion

matriz = [[1, 2, 3],[2,3,5],[1,4,7]]
print(matriz)
print(determinante(matriz))
            


    
