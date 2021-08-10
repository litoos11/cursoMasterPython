import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "172.17.0.2",
        user = "root",
        passwd = "Nomelase01",
        database = "db_master_python",
        port = 3306
        )

    cursor = database.cursor(buffered=True)
    return [database, cursor]
