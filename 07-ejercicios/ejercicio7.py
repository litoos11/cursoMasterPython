"""
    Ejercicio 7. Mostrar numeros pares que se encuentren entre 
    dos numero que introduce el usuairo.
"""

numero1 = int(input("Introduce el numero uno: "))
numero2 = int(input("Introduce el numero dos: "))
pares = []
impares = []
if numero1 < numero2:
    for num in range(numero1, (numero2 + 1)):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print(f"Los numeros pares son: {pares}")
    print(f"Los numeros impares son: {impares}")
else:
    print("EL numero 1 debe ser menor al numero2")

