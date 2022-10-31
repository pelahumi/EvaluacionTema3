from Pila import Pila

#Creamos las tres torres de hanoi como objetos pila

hanoi1 = Pila("Torre 1")
hanoi2 = Pila("Torre 2")
hanoi3 = Pila("Torre 3")

#Creamos una lista con 64 elementos 
elementos = []
for i in range (1,4):
    elementos.append(i)

#Los apilamos en la primera torre
long = len(elementos)
for i in range(long):
    hanoi1.apilar(elementos[long - i -1])

#Ahora creamos el algoritmo que resolvera el problema

def torres_hanoi(discos, origen, auxiliar, destino):

    if discos >= 1:
        torres_hanoi(discos - 1, origen, destino, auxiliar)
        mover(origen, destino)
        torres_hanoi(discos - 1, auxiliar, destino, origen)

    movimientos = 2**discos - 1 
    return destino

def mover(origen, destino):
    print(origen.en_cima(), "va a la ",destino.nombre)
    origen.desapilar()
    destino.apilar(origen.en_cima())

def main():
    torres_hanoi(3, hanoi1, hanoi2, hanoi3).barrido()



main()







        
        
    

