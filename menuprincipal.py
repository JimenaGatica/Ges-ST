import tkinter as tk
import usuarios
import reparaciones
import presupuestos
import consulta
import estado  # Importa el archivo estado.py

def mostrar_menu_principal(ventana_inicio):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Principal - Sistema de Gestión")
    ventana_menu.geometry("900x400+200+100")
    ventana_menu.configure(bg="snow2")  # Color de fondo

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()

    # Botones con texto y estilo mejorado
    boton_usuarios = tk.Button(ventana_menu, text="Crear Nuevo Usuario", command=usuarios.crear_usuario, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_usuarios.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

    boton_reparaciones = tk.Button(ventana_menu, text="Nueva Orden de Reparación", command=reparaciones.nueva_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_reparaciones.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    boton_presupuestos = tk.Button(ventana_menu, text="Presupuesto", command=presupuestos.presupuesto, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_presupuestos.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

    boton_consultar_reparacion = tk.Button(ventana_menu, text="Consultar Reparación", command=consulta.consultar_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_consultar_reparacion.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    boton_estado_reparacion = tk.Button(ventana_menu, text="Estado de Reparación", command=estado.gestion_estados, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_estado_reparacion.place(relx=0.25, rely=0.8, anchor=tk.CENTER)

    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_salir.place(relx=0.75, rely=0.8, anchor=tk.CENTER)