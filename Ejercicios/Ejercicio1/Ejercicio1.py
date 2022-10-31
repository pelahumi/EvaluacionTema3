from Pila import Pila, NodoPila

#Creamos las tres torres de hanoi como objetos pila

hanoi1 = Pila("Torre 1")
hanoi2 = Pila("Torre 2")
hanoi3 = Pila("Torre 3")

#Creamos una pila con los discos
for i in range (3,0,-1):
    if i < 4:
        a = NodoPila(i, i+1)
        hanoi1.apilar(a.info)
    else:
        a = NodoPila(i)
        hanoi1.apilar(a.info)


#Ahora creamos el algoritmo que resolvera el problema

def torres_hanoi(discos, origen, auxiliar, destino):

    if discos >= 1:
        torres_hanoi(discos - 1, origen, destino, auxiliar)
        mover(origen, destino)
        torres_hanoi(discos - 1, destino, origen, auxiliar)

def mover(origen, destino):
    print(origen.cima.info, "va a la ",destino.nombre)
    origen.desapilar()
    destino.apilar(origen.en_cima())

def main():
    torres_hanoi(3, hanoi1, hanoi2, hanoi3).barrido()

main()









        
        
    

