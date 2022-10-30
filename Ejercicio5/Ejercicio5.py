#Importamos la libreria hashlib
import hashlib


class Cifrado():
    def __init__(self, mensaje):
        self.mesaje = str(input("Introduce el mensaje que quieres enviar: ").encode("utf-8"))

    def cifrar(self):
        code = hashlib.blake2s()
        code.update(self.mesaje)
        cifrado = code.hexdigest()
        return cifrado
    
    def descifrar(self):
        encode = str(input("Introduce el mensaje a deescifrar: "))
        code = hashlib.blake2s()
        code.update(self.mensaje)

        if encode == code:
            print("El mensaje es: ",self.mesaje)
        else:
            print("El mensaje cifrado no coincide con el mensaje enviado")





 
            

