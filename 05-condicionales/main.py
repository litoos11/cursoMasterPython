#Condicional IF

#Ejemplo 1
print("#############Ejemplo 1############")
color = "rojo"

#color = input("Inserta el color")

if color == "rojo":
    print("Felicidades")
    print("El color es rojo")
else:
    print("El color es incorrecto")
"""    
#Operadores de comparación

== igual
!= diferente
<  menor
>  mayor
<=
>=

"""


print("\n#############Ejemplo 2############")
#year = 2020
year = input("En que año estamos?")

if int(year) >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año menor al 2021")
