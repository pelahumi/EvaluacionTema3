#Creamos la clase nodo
class Nodo():
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig

#Creamos la clase dato polinomio que crea un polinomio con valor y término
class DatoPolinomio():
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

#Creamos la clase polinomio que crea un polinomio de grado 0
class Polinomio():
    def __init__(self):
        self.termino_mayor = None
        self.grado = -1
