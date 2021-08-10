#Capturar excepciones y manejar errores en código
"""
try:
    nombre = input("¿Caul es tu nombre? ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, nombre no valido")
else:
    print("Ha funcionado correctamente")
finally:
    print("Fin del programa")
"""

"""
#Multiples excepciones
try:
    numero = int(input("Numero para elevar al cuadrado: "))
    print("El cuadrado es: " + str(numero * numero))
except TypeError:
    print("Convertir cadenas a enteros")
#except ValueError:
#    print("Introduce solo numeros")
except Exception as err:
    print(type(err))
    print("Error: ", type(err).__name__)
"""

#Exception personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad no es valida")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    elif len(nombre) > 10:
        raise ValueError("El nombre no puede exceder de 10 caracteres")
    else:
        print(f"Binevenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as err:
    print("Existe un error: ", err)
    
