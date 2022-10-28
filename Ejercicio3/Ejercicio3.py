#Creamos la clase naves
class Naves():
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    def dict(self):
        diccionario = {"Nombre" : self.nombre, "Largo" : self.largo, "Tripulacion" : self.tripulacion, "Pasajeros" : self.pasajeros}
        return diccionario

class Ejercito():
    def __init__(self):
        self.naves = []

    def listar(self, nave):
        self.naves.append(nave)
    


n1 = Naves("Halcon milenario", 123, 3, 9)

n2 = Naves("Estrella de la muerte", 13446, 3557, 3656)

n1.listado()
n2.listado()


