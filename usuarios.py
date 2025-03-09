import tkinter as tk
from tkinter import messagebox
import sqlite3

def crear_usuario():
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Crear Nuevo Usuario")

    # Campos para ingresar los datos del usuario
    nombre_label = tk.Label(ventana_crear_usuario, text="Nombre:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana_crear_usuario)
    nombre_entry.pack()

    usuario_label = tk.Label(ventana_crear_usuario, text="Usuario:")
    usuario_label.pack()
    usuario_entry = tk.Entry(ventana_crear_usuario)
    usuario_entry.pack()

    clave_label = tk.Label(ventana_crear_usuario, text="Contraseña:")
    clave_label.pack()
    clave_entry = tk.Entry(ventana_crear_usuario, show="*")
    clave_entry.pack()

    def guardar_usuario():
        nombre = nombre_entry.get()
        usuario = usuario_entry.get()
        clave = clave_entry.get()

        if not nombre or not usuario or not clave:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            conexion = sqlite3.connect("usuarios.db") #crea la base de datos si no existe
            cursor = conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, usuario TEXT, clave TEXT)")
            cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?)", (nombre, usuario, clave))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario creado correctamente")
            ventana_crear_usuario.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al crear el usuario: {e}")

    boton_guardar = tk.Button(ventana_crear_usuario, text="Guardar", command=guardar_usuario)
    boton_guardar.pack()