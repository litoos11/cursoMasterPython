"""
Comprobar tipo de objeto  de una lista, un string, un entero y un bool
y que imprima el tipo de dato de cada variable
"""

def traducir_tipo(tipo):
    respuesta = None
    if tipo == list:
        respuesta = "Lista"
    elif tipo == str:
        respuesta = "Cadena de texto"
    elif tipo == int:
        respuesta = "Entero"
    elif tipo == bool:
        respuesta = "Booleano"

    return respuesta


def comprobar_tipo(dato, tipo):
    prueba = isinstance(dato, tipo)
    respuesta = ""

    if prueba:
        respuesta = f"Esta variable es del tipo {traducir_tipo(tipo)}"
    else:
        respuesta = None

    return respuesta

lista = ["hola", 1]
titulo = "Hello world"
numero = 15
falso = True

print(comprobar_tipo(lista, list))
print(comprobar_tipo(titulo, str))
print(comprobar_tipo(numero, int))
print(comprobar_tipo(falso, bool))
