#Herencia
class Persona:

    """
        nombre
        apellidos
        altura
        edad
    """

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_altura(self):
        return self.altura

    def get_edad(self):
        return self.edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_altura(self, altura):
        self.altura = altura

    def set_edad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):
    """
        lenguajes
        experiencia
    """
    
    def __init__(self):
        self.lenguajes = "HTML, CSS, Javascript, PHP"
        self.experiencia = 5

    def get_lenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def reparar_pc(self):
        return "Estoy reparando tu pc"

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() 
        self.auditar_redes = "experto"
        self.experiencia = 7

    def auditoria(self):
        return "Estoy auditando redes"
