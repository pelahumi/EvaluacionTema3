from Pila import Pila

#Creamos las tres torres de hanoi como objetos pila

hanoi1 = Pila()
hanoi2 = Pila()
hanoi3 = Pila()

#Creamos una lista con 64 elementos 
elementos = []
for i in range (1,65):
    elementos.append(i)

#Los apilamos en la primera torre
long = len(elementos)
for i in range(long):
    hanoi1.apilar(elementos[long - i -1])

#Ahora creamos el algoritmo que resolvera el problema
def torres_hanoi(torre1, torre2, torre3):
    torre1 = hanoi1
    torre2 = hanoi2
    torre3 = hanoi3
    discos = 64
    if discos == 1:
        print(torre1.en_cima(), "va a ", torre3.
    

