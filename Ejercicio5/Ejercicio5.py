#Importamos la libreria hashlib
import hashlib


class Cifrado():
    def __init__(self):
        self.mensaje = input("Introduce el mensaje que quieres enviar: ").encode("utf-8")

    def cifrar(self):
        code = hashlib.sha256()
        code.update(self.mensaje)
        cifrado = code.hexdigest()
        return cifrado
    
    def descifrar(self):
        encode = str(input("Introduce el mensaje a descifrar: "))
        code = hashlib.sha256()
        code.update(self.mensaje)
        cifrado = code.hexdigest()

        if encode == cifrado:
            print("El mensaje es: ", self.mensaje)
        else:
            print("El mensaje cifrado no coincide con el mensaje enviado")





 
            

