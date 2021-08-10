"""
VARIABLES LOCALES Y GLOBALES:

"""

#GLOBALES
frase = "Esto es una frase"

print(frase)


def hola_mundo():
    frase = "Hola mundo!!"
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    print(year)
    
    global website
    website = "litoos11.com"

    print("Dentro: ", website)

    return "Año dentro " + str(year)
#hola_mundo()

print(hola_mundo())
print("Fuera ", website)
