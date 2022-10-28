import Ejercicio3
from Ejercicio3.Ejercicio3 import Ejercito, Naves

if __name__ == "__main__":
    halcon = Naves("Halcon milenario", 123, 5, 21)
    estrella = Naves("Estrella de la muerte", 34454, 34, 1344)

    naves = Ejercito()
    naves.listar(halcon)
    naves.listar(estrella)

    
