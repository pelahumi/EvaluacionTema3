from Ejercicio3 import Ejercito, Naves

if __name__ == "__main__":
    halcon = Naves("Halcon milenario", 34, 4, 10)
    estrella = Naves("Estrella de la muerte", 100000, 825.984, 1000000)
    caza = Naves("Caza TIE", 10, 1, 1)
    xwing = Naves("X-Wing", 16, 1, 2)
    destructor = Naves("Destructor Estelar", 1600, 37000, 40000)
    at = Naves("AT-AT", 30, 5, 5)
    lanzadera = Naves("Lanzadera Imperial", 20, 3, 5)
    reptador = Naves("Reptador de las arenas", 40, 50, 50)

    
    flota = Ejercito()
    flota.listar(halcon.dict())
    flota.listar(estrella.dict())
    flota.listar(caza.dict())
    flota.listar(xwing.dict())
    flota.listar(destructor.dict())
    flota.listar(at.dict())
    flota.listar(lanzadera.dict())
    flota.listar(reptador.dict())
    print(flota.naves)



