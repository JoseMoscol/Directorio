import sqlite3 as sql

class ConexcionDB():
    def __init__(self) -> None:
        self.base_datos = 'database/contacto.db'
        self.conexion = sql.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrarDB(self):
        self.conexion.commit()
        self.conexion.close()