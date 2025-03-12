import tkinter as tk
from tkinter import messagebox
import sqlite3
import menuprincipal

def verificar_credenciales():
    usuario = usuario_entry.get()
    clave = clave_entry.get()

    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))
        resultado = cursor.fetchone()
        conexion.close()
        if resultado:
            ventana_inicio.withdraw()
            menuprincipal.mostrar_menu_principal(ventana_inicio)
            clave_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", " Usuario o Clave incorrecta. Intente nuevamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al verificar credenciales: {e}")

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión - Sistema de Gestión")  # Título más llamativo
ventana_inicio.geometry("700x500")  # Ajuste de la geometría

# Etiqueta de bienvenida
bienvenida_label = tk.Label(ventana_inicio, text="Bienvenido a su Sistema de Gestión", font=("Arial", 16))
bienvenida_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Posición centrada

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana_inicio, text="Ingrese su Usuario y Contraseña", font=("Arial", 12))
instrucciones_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Etiqueta y entrada de usuario
usuario_label = tk.Label(ventana_inicio, text="Usuario:", font=("Arial", 12))
usuario_label.place(relx=0.2, rely=0.45, anchor=tk.W)
usuario_entry = tk.Entry(ventana_inicio, font=("Arial", 12))
usuario_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# Etiqueta y entrada de contraseña
clave_label = tk.Label(ventana_inicio, text="Contraseña:", font=("Arial", 12))
clave_label.place(relx=0.2, rely=0.55, anchor=tk.W)
clave_entry = tk.Entry(ventana_inicio, show="*", font=("Arial", 12))
clave_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Botón de iniciar sesión
boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales, font=("Arial", 12), bg="#B2EBF2")
boton_iniciar_sesion.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

ventana_inicio.mainloop()