"""
    LISTAS (Arrays)
    Son coleciones o conjuntos de datos/valores, bajo un unico nombre
"""

pelicula = "Batman"
#Definir listas
peliculas = ["batman", "spiderman", "superman"]
cantantes = list(('2pac', 'Drake', 'Jlove'))
anios = list(range(2020, 2050))
variada = ["Juan", 30, 4.5, True, "Text"]

"""
print(cantantes)
print(peliculas)
print(anios)
print(variada)
"""

"""
#Indices
peliculas[1] = "flash"
peliculas[2] = "Otra cosa"
print(peliculas[0])
print(peliculas[-1])
print(cantantes[1:3])
print(peliculas[1:])
"""

"""
#Añadir elementos a una listas
cantantes.append("Fase old")
cantantes.append("Otro cantante")
print(cantantes)
"""

"""
#Recorrer listas

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


print("\n***************LISTADO PELICULAS ***************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1}. {pelicula}")
"""

"""
#Listas multidimensionales

print("\n ***********LISTADO DE CONTACTOS*************")
contactos = [
        ['Antonio', 'antonio@litoos11.com'],
        ['luis', 'luis@litoos11.com'],
        ['Salvador', 'salvador@litoos11.com']
        ]
#print(contactos)
#print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
"""


