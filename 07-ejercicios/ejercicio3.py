"""
    Imprimir cuadrados de los 60 primeros numeros naturales
"""
#While
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1

#For
for contador in range(1, 61):
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
