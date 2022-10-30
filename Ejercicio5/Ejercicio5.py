#Importamos la libreria hashlib
import hashlib
from hmac import digest_size

class Cifrado():
    def __init__(self, mensaje):
        self.mesaje = str(input("Introduce el mensaje que quieres enviar: ").encode("utf-8"))
        self.cifrado = None

    def cifrar(self):
        code = hashlib.blake2s()
        code.update(self.mesaje)
        self.cifrado = code.hexdigest()
        return self.cifrado
    
    def descifrar(self):
        encode = str(input("Introduce el mensaje a deescifrar: "))
        descifrador = open("palabras.txt", "r")

        for x in descifrador.readlines():
            a = x.strip("\n").encode("utf-8")
            b = hashlib.blake2s(a).hexdigest()

        
        if a == encode:
            

