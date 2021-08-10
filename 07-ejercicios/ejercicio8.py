"""
    Ejercicio 8. Calcular el porcentaje de un numero introducido por
    el usuario asi como su porcentaje
"""

numero = int(input("Introduce un numero: "))
porcentaje = int(input(f"Que porcentaje quieres sacar de {numero}? "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")
