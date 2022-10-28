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

    def ordenar(self, lista):
        nombres = []
        for i in lista:
            nombres.append(i["Nombre"])
        nombres = sorted(nombres)
        return nombres

        


        
    






