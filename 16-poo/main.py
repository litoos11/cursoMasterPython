#POO

#Definir una clase (molde para crear mas objetos de ese tipo)

class Coche:
    #Atributos o propiedades
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Vocho"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    lugares = 2

    #métodos, acciones que hace el coche
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad

#fin de la clase

#Crear objetos de la clase
coche = Coche()
coche.setColor("amarillo")
coche.setModelo("Otro modelo")

print(coche.marca,coche.getModelo(),  coche.getColor())
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.velocidad)

#Crear mas objetos
print("******COCHE 2*********")
coche2 = Coche()
coche2.setColor("Gris")
print(coche2.getColor())
print(coche2.marca,coche2.getModelo(),  coche2.getColor())
