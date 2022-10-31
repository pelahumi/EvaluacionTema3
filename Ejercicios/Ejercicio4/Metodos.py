#Importamos las clases de Polinomio.py
from Ejercicios.Ejercicio4.Polinomio import Nodo, DatoPolinomio, Polinomio

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

def modificar_termino(polinomio, termino, valor):
    aux = polinomio.termino_mayor
    while (aux is not None) and (aux.info.termino != termino):
        aux = aux.sig
        aux.info.valor = valor
    
def obtener_valor(polinomio, termino):
    aux = polinomio.termino_mayor
    while (aux is not None) and (aux.info.termino > termino):
        aux = aux.sig
    if (aux is not None) and (aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0

def mostrar(polinomio):
    aux = polinomio.termino_mayor
    pol = ""
    if aux is not None:
        while aux is not None:
            signo = ""
            if aux.info.valor >= 0:
                signo += "+"
            pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
            aux = aux.sig
    return pol
    