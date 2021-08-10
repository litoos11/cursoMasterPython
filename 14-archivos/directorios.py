import os
import shutil


#crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el dir")

#eliminar dir
#os.rmdir("./mi_carpeta")

#copiar
"""
ruta_orifinal = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copytree(ruta_orifinal, ruta_nueva)

os.rmdir("./mi_carpeta_copiada")
"""
print("contenido de la carpeta")
contenido = os.listdir("./mi_carpeta")
#print(contenido)

for archivo in contenido:
    print("Fichero: " + archivo)

