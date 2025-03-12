import tkinter as tk
import usuarios
import reparaciones
import presupuestos
import consulta

def mostrar_menu_principal(ventana_inicio):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú")
    ventana_menu.geometry("600x600")

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()
        

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