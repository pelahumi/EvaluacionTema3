#Importamos las clases de Polinomio.py
from Polinomio import Nodo, DatoPolinomio, Polinomio

#Creamos las funciones

def agregar_termino(polinomio, termino, valor):
    aux = Nodo()
    dato = DatoPolinomio(valor, termino)
    aux.info = dato

    if termino > polinomio.grado:
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    
    else:
        act = polinomio.termino_mayor
        while (act.sig is not None) and (termino < act.sig.info.termino):
            act = act.sig
        aux.sig = act.sig
        act.sig = aux
