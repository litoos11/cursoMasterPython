"""
crear una lista con el contenido de esta tabla
Accion   Aventura   Deportes
GTA      Assians    Fifa 2021
COD      Crash      Pro 2021
PLUG     Prince     Moto G 
 Mostrar informacion ordenada
 """

tabla = [
        {
            "categoria": "Accion",
            "juegos": ["GTA", "COD", "PUG"]
        },
        {
            "categoria": "Aventura",
            "juegos": ["Assians", "Crash", "Prince"]
        },
        {
            "categoria": "Deportes",
            "juegos": ["Fifa", "Pro", "Moto G"]
        }
]

for categoria in tabla:
    print(f"---- {categoria['categoria']}")
    for juego in categoria['juegos']:
        print(f"{juego}")
