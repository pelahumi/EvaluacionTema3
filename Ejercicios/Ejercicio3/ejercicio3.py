#Creamos la clase naves
class Naves():
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        #El constructor contendrá los parámetros pedidos por el ejercicio
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    
    #Creamos un método que nos cree un diccionario con todos los parámetros de la nave
    def dict(self):
        diccionario = {"Nombre" : self.nombre, "Largo" : self.largo, "Tripulacion" : self.tripulacion, "Pasajeros" : self.pasajeros}
        return diccionario

#Creamos la clase que contendra a las naves pertenecientes a la clase anterior
class Ejercito():
    def __init__(self):
        #El constructor tendrá una lista vacía
        self.naves = []

    def listar(self, nave):
        #Con este método listamos las naves creadas como una lista de diccionarios
        self.naves.append(nave)

    def ordenar_nombres(self, lista):
        #Creamos una lista vacia que rellenamos con los nombres de las naves y despues ordenamos con la funcion sorted
        nombres = []
        for i in lista:
            nombres.append(i["Nombre"])
        nombres = sorted(nombres)
        return nombres
    
    def ordenar_largo(self, lista):
        #Hacemos lo mismo que en el método anterior, pero esta vez ordenamos en reversa
        largo = []
        for i in lista:
            largo.append(i["Largo"])
        largo.sort(reverse=True)
        return largo    
    
    def halcon_estrella(self, lista):
        #Hacemos un bucle que recorra la lista de diccionarios y si hay alguna nave con el nombre Halcon milenario o Estrella de la muerte nos devuelve una lista con los datos de la nave 
        naves = []
        for i in lista:
            if i["Nombre"] == "Halcon milenario":
                naves.append(i)
            
        for i in lista:
            if i["Nombre"] == "Estrella de la muerte":
                naves.append(i)
                
        return naves
    
    def mayor_pasajeros(self, lista):
        #Primero metemos los datos de longitud en una lista
        pasajeros = []
        for i in lista:
            pasajeros.append(i["Largo"])
        #Los ordenamos en reversa
        pasajeros.sort(reverse=True)
        max_pasaj = pasajeros[:5]
        return max_pasaj
        
    def mayor_tripulacion(self, lista):
        tripulacion = []
        for i in lista:
            tripulacion.append(i["Tripulacion"])
        for i in lista:
            if i["Tripulacion"] == max(tripulacion):
                return i["Nombre"]
            else:
                pass

    def at(self, lista):
        #Buscamos si en algun nombre contiene AT
        for i in lista:
            if "AT" in i["Nombre"]:
                return i
            else:
                pass
    
    def seis_pasajeros(self, lista):
        #Condicional para ver si alguna nave tiene capacidad para seis o mas pasajeros
        nave = []
        for i in lista:
            if i["Pasajeros"] >= 6:
                nave.append(i)
            else:
                pass
        return nave
    
    def mayor_y_menor(self, lista):
        #Buscamos y retornamos la nave más grande y más pequeña
        largo = []
        for i in lista:
            largo.append(i["Largo"])
        for i in lista:
            if i["Largo"] == max(largo):
                mayor = i
            elif i["Largo"] == min(largo):
                menor = i
            else:
                pass
        return mayor, menor