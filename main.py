import tkinter as tk
from tkinter import messagebox
import usuarios
import reparaciones
import presupuestos
import consulta
import sqlite3

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
            mostrar_menu_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al verificar credenciales: {e}")



def mostrar_menu_principal():
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú")
    ventana_menu.geometry("600x600")

    def volver_a_inicio():
        ventana_menu.destroy()  # Cierra la ventana del menú
        ventana_inicio.deiconify()  # Muestra la ventana de inicio de sesión
        clave_entry.delete(0, tk.END)  # Borra el contenido del campo de contraseña
         
    boton_usuarios = tk.Button(ventana_menu, text="Crear Nuevo Usuario", command=usuarios.crear_usuario)
    boton_usuarios.pack()

    boton_reparaciones = tk.Button(ventana_menu, text="Nueva Orden de Reparación", command=reparaciones.nueva_reparacion)
    boton_reparaciones.pack()

    boton_presupuestos = tk.Button(ventana_menu, text="Presupuesto", command=presupuestos.presupuesto)
    boton_presupuestos.pack()
    
    boton_consultar_reparacion = tk.Button(ventana_menu, text="Consultar Reparación", command=consulta.consultar_reparacion)
    boton_consultar_reparacion.pack()

    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio)
    boton_salir.pack()


ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("600x600")  

usuario_label = tk.Label(ventana_inicio, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_inicio)
usuario_entry.pack()

clave_label = tk.Label(ventana_inicio, text="Contraseña:")
clave_label.pack()
clave_entry = tk.Entry(ventana_inicio, show="*")  # Oculta la contraseña
clave_entry.pack()

boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales)
boton_iniciar_sesion.pack()

ventana_inicio.mainloop()