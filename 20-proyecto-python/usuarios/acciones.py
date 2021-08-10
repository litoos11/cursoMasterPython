import usuarios.usuario as user
import notas.acciones

class Acciones:

    def registro(self):
        print("Ok!! Identificate en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = user.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo pudimos registrarte.")
  
    def login(self):
        print("Ok!! Identificate en el sistema...")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = user.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema {login[5]}")
                self.proximasAcciones(login)
        except Exception as ex:
            print(type(ex))
            print(type(ex).__name__)
            print(f"Login incorrecto!!, Intentalo mas tarde.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: \n")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Ok {usuario[1]} vuelve pronto!")
            exit()
        else:
            print("Acción no valida, intenta de nuevo!!")
            self.proximasAcciones(usuario)
