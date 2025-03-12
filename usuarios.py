import tkinter as tk
from tkinter import messagebox
import sqlite3

def crear_usuario():
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Crear Nuevo Usuario - Sistema de Gestión")
    ventana_crear_usuario.geometry("900x400+200+200")
    ventana_crear_usuario.configure(bg="snow2")  # Color de fondo

    # Campos para ingresar los datos del usuario
    nombre_label = tk.Label(ventana_crear_usuario, text="Nombre:", font=("Arial", 12), bg="#E0F2F7")
    nombre_label.place(relx=0.2, rely=0.2, anchor=tk.W)
    nombre_entry = tk.Entry(ventana_crear_usuario, font=("Arial", 12))
    nombre_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    usuario_label = tk.Label(ventana_crear_usuario, text="Usuario:", font=("Arial", 12), bg="#E0F2F7")
    usuario_label.place(relx=0.2, rely=0.35, anchor=tk.W)
    usuario_entry = tk.Entry(ventana_crear_usuario, font=("Arial", 12))
    usuario_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    clave_label = tk.Label(ventana_crear_usuario, text="Contraseña:", font=("Arial", 12), bg="#E0F2F7")
    clave_label.place(relx=0.2, rely=0.5, anchor=tk.W)
    clave_entry = tk.Entry(ventana_crear_usuario, show="*", font=("Arial", 12))
    clave_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def guardar_usuario():
        nombre = nombre_entry.get()
        usuario = usuario_entry.get()
        clave = clave_entry.get()

        if not nombre or not usuario or not clave:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            conexion = sqlite3.connect("usuarios.db")  # crea la base de datos si no existe
            cursor = conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, usuario TEXT, clave TEXT)")
            cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?)", (nombre, usuario, clave))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario creado correctamente")
            ventana_crear_usuario.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al crear el usuario: {e}")

    boton_guardar = tk.Button(ventana_crear_usuario, text="Guardar", command=guardar_usuario, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_guardar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)