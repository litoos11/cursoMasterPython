import mysql.connector

#Conexion
database = mysql.connector.connect(
    host = "172.17.0.2",
    user = "root",
    passwd = "Nomelase01",
    database = "db_master_python"
)

#print(database)
cursor = database.cursor()

#Crar la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS db_master_python;")
cursor.execute("SHOW DATABASES;")

"""
for db in cursor:
    print(db)
"""

#Crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id INT(10) AUTO_INCREMENT NOT NULL,
        marca VARCHAR(40) NOT NULL,
        modelo VARCHAR(40) NOT NULL,
        precio FLOAT(10,2) NOT NULL,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")
