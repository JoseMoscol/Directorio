from .conexion_db import ConexcionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexcionDB()

    sql = """
    CREATE TABLE contacto(
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

    sql = "DROP TABLE contacto"

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

class Contacto():
    def __init__(self, nombre, apellido, telefono, correo):
        self.id_contacto = None
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def __str__(self) -> str:
        return f'Contacto({self.nombre}, {self.apellido}, {self.telefono}, {self.correo})'

def guardar(contacto):
    conexion = ConexcionDB()
    
    sql = f"""INSERT INTO contacto (nombre, apellido, telefono, correo) VALUES('{contacto.nombre}', '{contacto.apellido}', '{contacto.telefono}', '{contacto.correo}')""" 
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo = 'Conexion a Registro'
        mensaje = 'No exista tabla en base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexcionDB()

    lista_contactos = []

    sql = "SELECT * FROM contacto"

    try:
        conexion.cursor.execute(sql)
        lista_contactos = conexion.cursor.fetchall()
        conexion.cerrarDB()
    except:
        titulo = 'Conexion a Registro'
        mensaje = 'Crear tabla en la base de datos'
        messagebox.showerror(titulo, mensaje)
    
    return lista_contactos

def editar(contacto, id_contacto):
    conexion = ConexcionDB()

    sql = f"UPDATE contacto SET nombre = '{contacto.nombre}', apellido = '{contacto.apellido}', telefono = '{contacto.telefono}', correo = '{contacto.correo}' WHERE id_contacto = {id_contacto} "

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_contacto):
    conexion = ConexcionDB()

    sql = f'DELETE FROM contacto WHERE id_contacto = {id_contacto} '

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarDB()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se pudo eliminar del registro'
        messagebox.showerror(titulo, mensaje)

def buscar(nombre):
    conexion = ConexcionDB()

    lista_busqueda = []

    sql = f"SELECT * FROM contacto WHERE nombre like '{nombre}' "

    try:
        conexion.cursor.execute(sql)
        lista_busqueda = conexion.cursor.fetchall()
        conexion.cerrarDB()
    except:
        titulo = 'Buscar dato'
        mensaje = 'No se ha encontrado el contacto'
        messagebox.showerror(titulo, mensaje)
    
    return lista_busqueda