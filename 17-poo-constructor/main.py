from coche import Coche

carro = Coche("Rojo", "Chevrolet", "Corsa", 250, 240, 4)
carro1 = Coche("Gris", "Chevrolet", "Atos", 250, 240, 4)
carro2 = Coche("Verde", "Chevrolet", "Camaro", 250, 240, 4)
carro3 = Coche("Rojo", "Renault", "Rio", 250, 240, 4)

"""
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
"""

#Detectar tipado
carro3 = "str"
if type(carro3) == Coche:
    print("Es un objeto correcto ")
else:
    print("NO es un coche")

#Visibilidad (Público o provado)
"""
print(carro.soy_publico)
print(carro.getPrivado())
"""
