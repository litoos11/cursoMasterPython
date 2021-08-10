#importar modulo
import sqlite3

#Conexión
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

#crear cursor
cursor = conexion.cursor()

#crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, " +
"titulo VARCHAR(255), " +
"descripcion TEXT, " +
"precio INT(255)" +
")")
"""

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
);
""")


#Guardar cambios
conexion.commit()

#Insert datos
#cursor.execute("INSERT INTO productos VALUES (null, 'Segundo Producto', 'Descripción de mi producto', '500')")

#Borrar registros
cursor.execute("DELETE FROM Productos")
conexion.commit()

#Insertar muchos registro
productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("Xbox", "Consola", 1200),
    ("Telefono", "Super chido", 500),
    ("Apple fire", "De lo mas basico", 300)
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#Update actualizar producto
cursor.execute("UPDATE productos SET precio = 600 WHERE precio < 700;")
conexion.commit()

#Leer datos
cursor.execute("SELECT * FROM productos WHERE precio >= 500;")
productos = cursor.fetchall()

for producto in productos:
    print("Producto: ", producto[0])
    print("Nombre: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT descripcion FROM productos;")
producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()
