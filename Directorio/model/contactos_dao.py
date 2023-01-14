from .conexion_db import ConexcionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexcionDB()

    sql = """
    CREATE TABLE contactos(
        id_contacto INTEGER,
        nombre VARCHAR(30),
        apellido VARCHAR(30),
        telefono INTEGER,
        correo VARCHAR(50),
        PRIMARY KEY(id_contacto AUTOINCREMENT)
    )"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        titulo = 'Crear registro'
        msj = 'Tabla creada exitosamente'
        messagebox.showinfo(titulo,msj)
    except:
        titulo = 'Crear registro'
        msj = 'Tabla ya creada'
        messagebox.showwarning(titulo,msj)

def borrar_tabla():
    conexion = ConexcionDB()

    sql = "DROP TABLE contactos"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
        titulo = 'Borrar registro'
        msj = 'Tabla borrada exitosamente'
        messagebox.showinfo(titulo,msj)
    except:
        titulo = 'Borrar registro'
        msj = 'Tabla ya borrada'
        messagebox.showwarning(titulo,msj)
    