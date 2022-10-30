from ejercicio3 import Ejercito, Naves

def ejercicio3():
    #Creamos las naves como objetos de la clase Naves
    halcon = Naves("Halcon milenario", 34, 4, 10)
    estrella = Naves("Estrella de la muerte", 100000, 825984, 1000000)
    caza = Naves("Caza TIE", 10, 1, 1)
    xwing = Naves("X-Wing", 16, 1, 2)
    destructor = Naves("Destructor Estelar", 1600, 37000, 40000)
    at = Naves("AT-AT", 30, 5, 5)
    lanzadera = Naves("Lanzadera Imperial", 20, 3, 5)
    reptador = Naves("Reptador de las arenas", 40, 50, 50)

    #Enlistamos las naves como lista de diccionarios en un objeto de la clase 
    flota = Ejercito()
    flota.listar(halcon.dict())
    flota.listar(estrella.dict())
    flota.listar(caza.dict())
    flota.listar(xwing.dict())
    flota.listar(destructor.dict())
    flota.listar(at.dict())
    flota.listar(lanzadera.dict())
    flota.listar(reptador.dict())

    #Apartado 1:
    print("Listado ordenado por nombre de manera ascendente y por longitud de manera descendente")
    print(flota.ordenar_nombres(flota.naves))
    print(flota.ordenar_largo(flota.naves))
    print("\n")

    #Apartado 2:
    print("Información Halcón Milenario y de la Estrella de la Muerte: ")
    print(flota.halcon_estrella(flota.naves))
    print("\n")

    #Apartado3:
    print("5 naves con mayor capacidad: ")
    print(flota.mayor_pasajeros(flota.naves))
    print("\n")

    #Apartado 4:
    print("Nave con mayor tripulación: ")
    print(flota.mayor_tripulacion(flota.naves))
    print("\n")

    #Apartado 5:
    print("Hay alguna nave que empiece por AT: ")
    print(flota.at(flota.naves))
    print("\n")

    #Apartado 6:
    print("Naves que pueden llevar 6 o más pasajeros: ")
    print(flota.seis_pasajeros(flota.naves))
    print("\n")
    
    #Apartado 7:
    print("Inforamción de la nave más pequeña y de la más grande: ")
    print(flota.mayor_y_menor(flota.naves))



