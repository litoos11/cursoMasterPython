"""
    FUNCIONES:
        
    def nombre_de_funcion(parametros):
        #Bloque de código ejecutado dentro de la funcion

    nombre_de_funcion(parametro1)
    nombre_de_funcion(parametro2)
"""

#Ejemplo 1
"""
print("###Ejemplo de funcion 1###")

def muestra_nombre():
    print("nombre")


muestra_nombre()
"""

# Ejemplo 2: parametrosi
"""
print("###Ejemplo de funcion 2###")

def mostrar_tu_nombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    
    if edad >= 18:
        print("Y eres mayor de edad")
nombre = input(f"Introduce tu nombre: ")
edad = int(input(f"Introduce tu edad: "))
mostrar_tu_nombre(nombre, edad)
"""

# Ejemplo 3: parametros
"""
print("###Ejemplo de funcion 3###")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")

num = int(input("introduce el número que desea hacer la tabla: "))
tabla(num)

for numero_tabla in range(1, 11):
    tabla(numero_tabla)

"""

"""
print("###Ejemplo de funcion 4###")

#Parametros opcionales

def get_empleado(nombre, curp=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if curp != None:
        print(f"CURP: {curp}")

get_empleado("Juan", "OISA860412") 
"""

"""
print("###Ejemplo de funcion 5###")
#Parametros opcionales y return a devolver datos
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Angel"))
"""


"""
#Ejemplo 6
print("###Ejemplo de funcion 6###")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)    
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi) 
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena

print(calculadora(2, 15, True))
"""

"""
print("###Ejemplo de funcion 7###")

def get_nombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def get_apellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelve_todo(nombre, apellidos):
    texto = get_nombre(nombre) + "\n" + get_apellidos(apellidos)
    return texto

print(devuelve_todo("Angel", "Ortiz"))
"""


print("###Ejemplo de funcion 8###")
#Ejemplo 8 Funciones lambda

dime_el_anio = lambda anio: f"EL año es: {anio * 2}"

print(dime_el_anio(2035))
