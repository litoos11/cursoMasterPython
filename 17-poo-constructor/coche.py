class Coche:
    #Atributos o propiedades
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Vocho"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    lugares = 2

    soy_publico = "Soy publico"
    __soy_privado = "Soy privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, lugares):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad  = velocidad
        self.caballaje = caballaje
        self.lugares = lugares

    #métodos, acciones que hace el coche
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getVelocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad += 1

    def setCaballaje(self, caballaje):
        self.caballaje= caballaje

    def getCaballaje(self):
        return self.caballaje

    def setLugares(self, lugares):
        self.lugares = lugares

    def getLugares(self):
        return self.lugares

    def frenar(self):
        self.velocidad -= 1
    
    def getPrivado(self):
        return self.__soy_privado

    def getInfo(self):
        info = " --- Información del coche --- "
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad()) + " km/h"

        return info

    
#fin de la clase
