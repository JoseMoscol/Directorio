import tkinter as tk
from tkinter import ttk, messagebox
from model.contactos_dao import crear_tabla, borrar_tabla
from model.contactos_dao import Contacto, guardar, listar, editar, eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_incicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_incicio)

    menu_incicio.add_command(label='Crear directorio', command=crear_tabla)
    menu_incicio.add_command(label='Eliminar directorio', command=borrar_tabla)
    menu_incicio.add_command(label='Salir directorio')

    barra_menu.add_cascade(label='Consultas')

    barra_menu.add_cascade(label='Configuracion')

    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root =  root
        self.pack()
        #self.config(bg='green')
        self.id_contacto = None

        self.campos_contactos()
        self.deshabilitar_campos()
        self.tabla_contactos()

    def campos_contactos(self):
        #Label para nombre
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        #Label apellido
        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Times New Roman', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)
        #Label telefono
        self.label_telefono = tk.Label(self, text="Telefono: ")
        self.label_telefono.config(font=('Times New Roman', 12, 'bold'))
        self.label_telefono.grid(row=0, column=2, padx=10, pady=10)
        #Label correo
        self.label_correo = tk.Label(self, text="Correo: ")
        self.label_correo.config(font=('Times New Roman', 12, 'bold'))
        self.label_correo.grid(row=1, column=2, padx=10, pady=10)

        #Entry nombre
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=23,font=('Times New Roman', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=1)
        #Entry apellido
        self.mi_apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.mi_apellido)
        self.entry_apellido.config(width=23,font=('Times New Roman', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10, columnspan=1)
        #Entry telefono
        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.mi_telefono)
        self.entry_telefono.config(width=23,font=('Times New Roman', 12))
        self.entry_telefono.grid(row=0, column=3, padx=10, pady=10, columnspan=1)
        #Entry correo
        self.mi_correo = tk.StringVar()
        self.entry_correo = tk.Entry(self, textvariable=self.mi_correo)
        self.entry_correo.config(width=23,font=('Times New Roman', 12))
        self.entry_correo.grid(row=1, column=3, padx=10, pady=10, columnspan=1)

        #Entry de buscar
        self.mi_busquedad = tk.StringVar()
        self.entry_buscar = tk.Entry(self, textvariable=self.mi_busquedad)
        self.entry_buscar.config(width=23,font=('Times New Roman', 12))
        self.entry_buscar.grid(row=4, column=1, padx=10, pady=10, columnspan=1)

        #Boton de nuevo
        self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='SpringGreen3', cursor='hand2', activebackground='SeaGreen2')
        self.boton_nuevo.grid(row=2, column=0, padx=10, pady=10)
        #Boton de guardar
        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='DodgerBlue2', cursor='hand2', activebackground='turquoise2')
        self.boton_guardar.grid(row=2, column=1, padx=10, pady=10)
        #Boton de cancelar
        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='IndianRed2', cursor='hand2', activebackground='RosyBrown2')
        self.boton_cancelar.grid(row=2, column=2, padx=10, pady=10)
        #Boton de editar
        self.boton_editar = tk.Button(self, text='Editar',command=self.editar_datos)
        self.boton_editar.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='DodgerBlue2', cursor='hand2', activebackground='turquoise2')
        self.boton_editar.grid(row=2, column=3, padx=10, pady=10)
        

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_telefono.set('')
        self.mi_correo.set('')

        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_correo.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_contacto = None

        self.mi_nombre.set('')
        self.mi_apellido.set('')
        self.mi_telefono.set('')
        self.mi_correo.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_correo.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        contact = Contacto(
            self.mi_nombre.get(),
            self.mi_apellido.get(),
            self.mi_telefono.get(),
            self.mi_correo.get()
        )

        if self.id_contacto == None:
            guardar(contact)
        else:
            editar(contact, self.id_contacto)

        self.tabla_contactos()

        self.deshabilitar_campos()

    def tabla_contactos(self):
        self.lista_contactos = listar()
        self.lista_contactos.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Apellido', 'Telefono', 'Correo'))
        self.tabla.grid(row=3, column=0, columnspan=4,  sticky='nse')

        #Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=3, column=3, sticky='nse')
        self.tabla.config(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='APELLIDO')
        self.tabla.heading('#3', text='TELEFONO')
        self.tabla.heading('#4', text='CORREO')

        for p in self.lista_contactos:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4]))

        #Boton de buscar
        self.boton_buscar = tk.Button(self, text='Buscar')
        self.boton_buscar.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='SpringGreen3', cursor='hand2', activebackground='SeaGreen2')
        self.boton_buscar.grid(row=4, column=0, padx=10, pady=10)

        #Boton de eliminar
        self.boton_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=('Times New Roman', 12, 'bold'), fg='white', bg='IndianRed2', cursor='hand2', activebackground='RosyBrown2')
        self.boton_eliminar.grid(row=4, column=2, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_contacto = self.tabla.item(self.tabla.selection())['text']
            self.nombre_contacto = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.apellido_contacto = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.telefono_contacto = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.correo_contacto = self.tabla.item(
                self.tabla.selection())['values'][3]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_contacto)
            self.entry_apellido.insert(0, self.apellido_contacto)
            self.entry_telefono.insert(0, self.telefono_contacto)
            self.entry_correo.insert(0, self.correo_contacto)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo,mensaje)

    def eliminar_datos(self):
        try:
            self.id_contacto = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_contacto)

            self.tabla_contactos()
            self.id_contacto = None
        except:
            titulo = 'Eliminar un Registro'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)