#Creamos la clase nodo
class Nodo():
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig

class DatoPolinomio():
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino