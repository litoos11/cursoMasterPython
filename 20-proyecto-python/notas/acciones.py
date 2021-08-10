import notas.nota as model

class Acciones:

    def crear(self, usuario):
        print(f"\nOk, {usuario[1]}!! Vamos a crear una nueva nota..:")
        
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        nota = model.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo de ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"Ok, {usuario[1]}!! Aquí tienes tus notas: ")

        nota = model.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n****************************************")
            print(nota[2])
            print(nota[3])

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a eliminar notas")

        titulo = input("introduce el título de la nota a eliminar: ")

        nota = model.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos eliminado la nota: {nota.titulo}")
        else:
            print("No se ha eliminado la nota, intenta mas tarde!")
