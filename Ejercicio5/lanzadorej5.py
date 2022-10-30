from ejercicio5 import Cifrado

def ejercicio5():
    mensaje = Cifrado()

    #Ciframos el mensaje
    print("El mensaje cifrado es:")
    print(mensaje.cifrar())

    #Desciframos el mensaje
    print(mensaje.descifrar())

ejercicio5()