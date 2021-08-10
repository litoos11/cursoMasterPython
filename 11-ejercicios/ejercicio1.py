"""
    #1.- Hacer un programa que tenga una lista de 8 numeros
        enteros y haga lo siguiente:
        -Recorrer la lista y mostarla
        -Hacer funcion que recorra la lista y devuelva un string
        -Ordenarla y mostrarla
        -Motrar su longitud
        -Buscar algún elemento que el usuario pida por teclado
"""

#Crear lista
numeros = [12, 15, 10, 11, 1, 15]

def mostrar_list(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado +=  "\n"
    return resultado

#recorrer y mostrar 
"""
print("############ RECORRER Y MOSTRAR ############")
for numero in numeros:
    print(numero)
"""

print(mostrar_list(numeros))
#print(mostrar_list(["Angel", "Juan", "Eymard", "Felix", "Salvador"]))

#ordenarlo y mostrarlo
print("############ ORDENAR Y MOSTRAR  ############")
numeros.sort()
print(mostrar_list(numeros))

#mostrat longitud
print("############ MOSTRAR LONGITU  ############")
print(len(numeros))

#busqueda en la lista
print("############ BUSCAR ELEMNTO INTRODUCIDO POR TECLADO ############")

buscar = int(input("Introduce el número: "))
comprobar = isinstance(buscar, int)
while not comprobar or buscar <= 0:
    buscar = int(input("Introduce el número: "))
else:
    print(f"Has introducido el {buscar}")

print(f"##### Buscar en la lista el número {buscar} #####")

buscado = numeros.index(buscar)

print(f"El número buscado existe en la lista, es el índice: {buscado}")
