import tkinter as tk
import reparaciones
import consulta

def mostrar_menu_atencion_publico(ventana_inicio):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Atención al Público - Sistema de Gestión")
    ventana_menu.geometry("900x400+200+100")
    ventana_menu.configure(bg="snow2")

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()

    boton_reparaciones = tk.Button(ventana_menu, text="Nueva Orden de Reparación", command=reparaciones.nueva_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_reparaciones.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

    boton_consultar_reparacion = tk.Button(ventana_menu, text="Consultar Reparación", command=consulta.consultar_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_consultar_reparacion.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_salir.place(relx=0.5, rely=0.5, anchor=tk.CENTER)