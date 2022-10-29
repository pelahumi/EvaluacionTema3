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

    def ordenar_nombres(self, lista):
        nombres = []
        for i in lista:
            nombres.append(i["Nombre"])
        nombres = sorted(nombres)
        return nombres
    
    def ordenar_largo(self, lista):
        largo = []
        for i in lista:
            largo.append(i["Largo"])
        largo.sort(reverse=True)
        return largo    
    
    def halcon_estrella(self, lista):
        naves = []
        for i in lista:
            if i["Nombre"] == "Halcon milenario":
                naves.append(i)
            else:
                print("No se ha encontrado el Halcon milenario")
            
        for i in lista:
            if i["Nombre"] == "Estrella de la muerte":
                naves.append(i)
            else:
                print("No se ha encontrado la Estrella de la muerte")
        return naves
    
    def mayor_pasajeros(self, lista):
        pasajeros = []
        for i in lista:
            pasajeros.append(i["Largo"])
        pasajeros.sort(reverse=True)
        max_pasaj = pasajeros[:5]
        return max_pasaj
        
    def mayor_tripulacion(self, lista):
        tripulacion = []
        for i in lista:
            tripulacion.append(i["Tripulacion"])
        sol = max(tripulacion)
        return sol
    


        


        
    






