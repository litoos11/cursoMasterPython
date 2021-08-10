
nombre = "litoos11"

#Genrales
print(nombre)
print(type(nombre))


#Detectar tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Es un string")
else:
    print("NO es una cadena")

if not isinstance(nombre, float):
    print("La variable no es número con decimales")


#Limpiar espacios
frase = "    ejemplo    de espacios"
print(frase)
print(frase.strip())

#Eliminar variables
year = 2056
print(year)
del year
#print(year)

#Comprobar varibles vacias
texto = "  FFF  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ", len(texto))

#Encontrar carecteres
frase = "La vida es bella"
print(frase.find("vida"))

#Remplazar palabras en un string
nueva_frase = frase.replace("vida", "caca")
print(nueva_frase)

#Mayusculas a minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())
