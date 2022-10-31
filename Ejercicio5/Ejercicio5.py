#Importamos la libreria hashlib
import hashlib

#Creamos una clase que tenga como atributo el mensaje que se quiere cifrar
class Cifrado():
    def __init__(self):
        #Pedimos por pantalla el mensaje que se quiere cifrar
        self.mensaje = input("Introduce el mensaje que quieres enviar: ").encode("utf-8") #Añadimos encode utf-8 para que también lea los acentos

    #Creamos un método para que nos cifre el mensaje
    def cifrar(self):
        #Code es una variable que almacena una función que cifra en sha256, nos devuelve el mensaje cifrado en 256 carácteres
        code = hashlib.sha256() #Está vacío
        code.update(self.mensaje) #Añadimos el mensaje a cifrar
        cifrado = code.hexdigest() #Hacemos un "resumen"
        return cifrado
    
    #Creamos un método que pedirá un mensaje cifrado y nos dirá si es el mensaje enviado o no
    def descifrar(self):
        encode = str(input("Introduce el mensaje a descifrar: "))
        code = hashlib.sha256()
        code.update(self.mensaje)
        cifrado = code.hexdigest()

        if encode == cifrado:
            print("El mensaje es: ", self.mensaje)
        else:
            print("El mensaje cifrado no coincide con el mensaje enviado")





 
            

