"""
Proyecto python y mysql:
    -Abrir un asistente
    -Login o registro
    -Si registro, creara un usuario en la bd
    -Si login, identifica usuario y nos pregunta 
    -Crear nota, mostrar nota, eliminar nota.
"""

from usuarios import acciones


print("""
Acciones disponibles:
    - Registro
    - Login
        """)

hazEl = acciones.Acciones() 

accion = input("¿Que desea hacer?: ")
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
