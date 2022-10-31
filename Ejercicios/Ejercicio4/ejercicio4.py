#Importamos los ficheros que necesitaremos
from Ejercicios.Ejercicio4.Metodos import *


def restar(pol1, pol2):
    aux = Polinomio()
    mayor = pol1 if (pol1.grado > pol2.grado) else pol2
    for i in range(0, mayor.grado + 1):
        total = obtener_valor(pol1, i) - obtener_valor(pol2, i)
        if total != 0:
            agregar_termino(aux, i, total)
    return aux

def dividir(pol1, pol2):
    aux = Polinomio()
    poli1 = pol1.termino_mayor
    while poli1 is not None:
        poli2 = pol2.termino_mayor
        while poli2 is not None:
            termino = poli1.info.termino - poli2.info.termino
            valor =  poli1.info.valor // poli2.info.valor
            if obtener_valor(aux, termino) != 0:
                valor += obtener_valor(aux, termino)
                modificar_termino(aux, termino, valor)
            else:
                agregar_termino(aux, termino, valor)
            poli2 = poli2.sig
        poli1 = poli1.sig
    return aux

def eliminar(polinomio, termino):
    pol = polinomio.termino_mayor
    while pol is not None:
        termino_pol = pol.info.termino
        if termino_pol == termino:
            pol.info.valor = 0
            print("Se elimino el término")
            return
        else:
            pol = pol.sig

def existe(polinomio, termino):
    pol = polinomio.termino_mayor
    while pol is not None:
        termino_pol = pol.info.termino
        if termino_pol == termino:
            return pol.info.valor
        elif termino_pol is None:
            return False
        else:
            pol = pol.sig     