"""
    Ejercicio 9. Pedir numeros al usuario hasta meter el numero 111
"""

contador = 1
numeros = []
while contador < 100:
    numero = int(input("Introduce un número: "))

    if numero == 111:
        break
    else:
        numeros.append(numero)

print(f"Has introducido los numeros: {numeros}")
