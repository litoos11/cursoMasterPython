"""
    Ejercicio 5: Mostrar numeros entre dos numeros introducidos por el usuario
"""

numero1 = int(input("Introduce el numero uno: "))
numero2 = int(input("Introduce el numero dos "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        print(contador)
else:
    print("El número uno debe ser menor al número dos")
