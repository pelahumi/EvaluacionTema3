#Importamos los ficheros que necesitaremos
from Metodos import *


def restar(pol1, pol2):
    aux = Polinomio()
    mayor = pol1 if (pol1.grado > pol2.grado) else pol2
    for i in range(0, mayor.grado + 1):
        total = obtener_valor(pol1, i) - obtener_valor(pol2, i)
        if total != 0:
            agregar_termino(aux, i, total)
    return aux