import tkinter as tk
import presupuestos
import consulta
import estado

def mostrar_menu_tecnico(ventana_inicio):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Técnico - Sistema de Gestión")
    ventana_menu.geometry("900x400+200+100")
    ventana_menu.configure(bg="snow2")

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()


    bienvenidatecnico_label = tk.Label(ventana_menu, text="Bienvenido a al gestión Técnica", font=("Arial", 16), bg="snow2")
    bienvenidatecnico_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)




    boton_presupuestos = tk.Button(ventana_menu, text="Presupuesto", command=presupuestos.presupuesto, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_presupuestos.place(relx=0.25, rely=0.4, anchor=tk.CENTER)

    boton_consultar_reparacion = tk.Button(ventana_menu, text="Consultar Reparación", command=consulta.consultar_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_consultar_reparacion.place(relx=0.75, rely=0.4, anchor=tk.CENTER)

    boton_estado_reparacion = tk.Button(ventana_menu, text="Estado de Reparación", command=estado.gestion_estados, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_estado_reparacion.place(relx=0.25, rely=0.7, anchor=tk.CENTER)

    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 12), bg="#FFC107", padx=20, pady=10)
    boton_salir.place(relx=0.75, rely=0.7, anchor=tk.CENTER)