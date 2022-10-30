#Creamos la clase nodo
from distutils.log import info


class Nodo():
    def __init__(self, info=None, sig=None):
        self.info = info
        self.sig = sig