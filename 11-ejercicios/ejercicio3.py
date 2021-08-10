"""
comprobar si una variable esta vacia y si esta vacia rellenarla con
texto en minusculas y mostrarlo en mayusculas
"""

text = ""

if len(text.strip()) <= 0:
    #mostrar el text
    text = "ejemplo de un texto en minusculas"
    print(text.upper())
else:
    print(f"La variable tiene contenido {text}")
