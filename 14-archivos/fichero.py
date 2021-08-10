from io import open
import pathlib
import shutil
import os
import os.path

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/main.txt"
#print(ruta)

archivo = open(ruta, "a+")

#escribir en archivo
#archivo.write("** desde python **\n")

#cerrar archivo
archivo.close()

#Leer contenido
ruta = str(pathlib.Path().absolute()) + "/main.txt"
archivo_lectura = open(ruta, "r")

#contenido = archivo_lectura.read()

#print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for linea in lista:
    linea_frase = linea.split()
    #print(linea_frase)
    #print("- " + linea.upper().center(100)) 


#copiar archivo
"""
ruta_orifinal = str(pathlib.Path().absolute()) + "/main.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/main_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/07-ejercicios/main_copiado.txt" 

shutil.copyfile(ruta_orifinal, ruta_alternativa)
"""

#mover (renombrar)
"""
ruta_orifinal = str(pathlib.Path().absolute()) + "/main.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/main_copiado_nuevo.txt"

shutil.move(ruta_orifinal, ruta_nueva)
"""

#Eliminar
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/main_copiado_nuevo.txt"
os.remove(ruta_nueva)
"""

#Comprobar si existe
#print(os.path.abspath(".../"))

ruta_comprobar = os.path.abspath("./") + "/main_texto.txt"
ruta_comprobar = "./main.txt"
print(ruta_comprobar)


if os.path.isfile(ruta_comprobar):
    print("si existe el archivo")
else:
    print("no existe el archivo")

