"""
    Ejercicion 10. Calcular numero de alumnos aprobados y reprobados
    de acuerdo a sus notas introducidas
"""
contador = 1
aprobados = 0
reprobados = 0
alumons = int(input("Cuantos alumnos son? "))

while contador <= alumons:
    calificacion = int(input(f"Introduce la calificacion del \"alumno {contador}\"  "))
    
    if calificacion > 5:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    contador = contador + 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
