import clases
#from clases import Persona

persona = clases.Persona()
persona.set_nombre("Angel")
persona.set_apellidos("Ortiz")
persona.set_altura("165 cm")
persona.set_edad(34)

print(f"La persona es: {persona.get_nombre()} {persona.get_apellidos()}")
print(persona.hablar())
print("*****-----------------*****\n")

informatico = clases.Informatico()
informatico.set_nombre("Litoos11")
informatico.set_apellidos("Ortiz")

print(f"El informatico es: {informatico.get_nombre()} {informatico.get_apellidos()}") 
print(informatico.get_lenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("*****-----------------*****\n")

tecnico = clases.TecnicoRedes()
tecnico.set_nombre("Juan")
print(tecnico.auditar_redes, tecnico.get_nombre(), tecnico.get_lenguajes())

