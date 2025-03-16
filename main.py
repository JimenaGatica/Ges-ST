import tkinter as tk
from tkinter import messagebox
import sqlite3
import menuprincipal
import menutecnico
import menuatpu

def verificar_credenciales():
    usuario = usuario_entry.get()
    clave = clave_entry.get()

    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT rol FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            rol_usuario = resultado[0]
            ventana_inicio.withdraw()
            if rol_usuario == "Administrador":
                menuprincipal.mostrar_menu_principal(ventana_inicio)
            elif rol_usuario == "Técnico":
                menutecnico.mostrar_menu_tecnico(ventana_inicio)
            elif rol_usuario == "Atención al Público":
                menuatpu.mostrar_menu_atencion_publico(ventana_inicio)
            clave_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", " Usuario o Clave incorrecta. Intente nuevamente.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al verificar credenciales: {e}")

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión - Sistema de Gestión")
ventana_inicio.geometry("1350x695-0+0")
#ventana_inicio.state('zoomed')  # Maximiza la ventana

bienvenida_label = tk.Label(ventana_inicio, text="Bienvenido a su Sistema de Gestión", font=("Arial", 25))
bienvenida_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

instrucciones_label = tk.Label(ventana_inicio, text="Ingrese su Usuario y Contraseña", font=("Arial", 20))
instrucciones_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

usuario_label = tk.Label(ventana_inicio, text="Usuario:", font=("Arial", 17))
usuario_label.place(relx=0.2, rely=0.55, anchor=tk.W)
usuario_entry = tk.Entry(ventana_inicio, font=("Arial", 14))
usuario_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

clave_label = tk.Label(ventana_inicio, text="Contraseña:", font=("Arial", 17))
clave_label.place(relx=0.2, rely=0.65, anchor=tk.W)
clave_entry = tk.Entry(ventana_inicio, show="*", font=("Arial", 14))
clave_entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales, font=("Arial", 16), bg="#B2EBF2")
boton_iniciar_sesion.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

ventana_inicio.mainloop()