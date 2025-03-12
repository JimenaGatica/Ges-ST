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
            menuprincipal.mostrar_menu_principal(ventana_inicio) #llama a la funcion del archivo menuprincipal.py
            clave_entry.delete(0, tk.END) #limpia la contraseña
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al verificar credenciales: {e}")

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("600x600")

usuario_label = tk.Label(ventana_inicio, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_inicio)
usuario_entry.pack()

clave_label = tk.Label(ventana_inicio, text="Contraseña:")
clave_label.pack()
clave_entry = tk.Entry(ventana_inicio, show="*")
clave_entry.pack()

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack()

ventana_inicio.mainloop()