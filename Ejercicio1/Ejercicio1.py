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
def torres_hanoi(discos):
    torre1 = hanoi1
    torre2 = hanoi2
    torre3 = hanoi3

    cima = torre1.en_cima()
    cima2 = torre2.en_cima()
    cima3 = torre3.en_cima()
    if discos == 1:
        print(torre1.en_cima(), "va a la torre 3")
    else:
        if (cima < cima2) or (cima2 is None):
            torre2.apilar(cima)
            torre1.desapilar()
        elif (cima < cima3) or (cima3 is None):
            torre3.apilar(cima)
            torre1.desapilar()
        elif (cima2 < cima3) and (cima2 > cima):
            torre3.apilar(cima2)
            torre2.desapilar()
        elif (cima2 < cima) and (cima2 > cima3):
            torre1.apilar(cima2)
            torre2.desapilar()
        elif (cima3 < cima


        
        
    

