"""
    Almacena conjunto de valores con clave - valores
"""

persona = {
        "nombre": "Juan",
        "apellidos": "Ortiz",
        "web": "litoos11.com"
        }

#print(persona)
#print(persona["web"])

#lista con diccionarios
contactos = [
        {
            'nombre': 'Litos',
            'email': 'litos@litoos11.com'
        },
        {
            'nombre': 'Luis',
            'email': 'luis@litoos11.com'
        },
        {
            'nombre': 'Jose',
            'email': 'Jose@litoos11.com'
        }
        ]

contactos[0]['nombre'] = "Josesito"
print(contactos[0]['nombre'])

print("\nListado de contactos: ")

print("*----------------------------*")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email de contacto: {contacto['email']}")
    print("*----------------------------*")
