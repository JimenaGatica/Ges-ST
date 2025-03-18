import tkinter as tk
import presupuestos
import consulta
import estado

def mostrar_menu_tecnico(ventana_inicio):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Técnico - Sistema de Gestión")
    ventana_menu.state('zoomed')
    ventana_menu.configure(bg="snow2")

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()

    # Título principal
    bienvenidatecnico_label = tk.Label(ventana_menu, text="Bienvenido a la Gestión Técnica", font=("Arial", 22, "bold"), bg="snow2")
    bienvenidatecnico_label.pack(pady=20)

    # Subtítulo
    operaciones_label = tk.Label(ventana_menu, text="Usted como técnico podrá realizar las siguientes operaciones:", font=("Arial", 18), bg="snow2")
    operaciones_label.pack(pady=10)

    
    # Opción 1: Modificar estado
    modificar_estado_label=tk.Label(ventana_menu, text="Modificar el estado de la Reparación", font=("Arial", 16), bg="snow2")
    modificar_estado_label.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
    
    boton_estado_reparacion = tk.Button(ventana_menu, text="Modificar Estado", command=estado.modificar_estado, font=("Arial", 16), bg="#B2EBF2")
    boton_estado_reparacion.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    # Opción 2: Consultar reparación
    consultar_reparacio_label=tk.Label(ventana_menu, text= "Ver toda la informacioón de la Orden de Reparación", font=("Arial", 16), bg="snow2")
    consultar_reparacio_label.place(relx=0.25, rely=0.45, anchor=tk.CENTER)
    
    boton_consultar_reparacion = tk.Button(ventana_menu, text="Ver Orden de Reparación", command=consulta.consultar_reparacion, font=("Arial", 16), bg="#B2EBF2")
    boton_consultar_reparacion.place(relx=0.7, rely=0.45, anchor=tk.CENTER)

    # Opción 3: Crear presupuesto
    crear_presupuesto_label=tk.Label(ventana_menu, text= "Crear y agregar Presupuesto a Ordenes de Reparación", font=("Arial", 16), bg="snow2")
    crear_presupuesto_label.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
    
    boton_presupuesto = tk.Button(ventana_menu, text="Presupuesto", command=presupuestos.presupuesto, font=("Arial", 16), bg="#B2EBF2")
    boton_presupuesto.place(relx=0.7, rely=0.6, anchor=tk.CENTER)


    # Botón Salir
    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 16), bg="#FFC107", padx=20, pady=10)
    boton_salir.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    
    #tk.Label(consultar_reparacion_frame, text="Consultar orden de Reparación", font=("Arial", 12), bg="snow2", anchor="w").grid(row=0, column=0, sticky="w")
    #boton_consultar_reparacion = tk.Button(consultar_reparacion_frame, text="Consultar Reparación", command=consulta.consultar_reparacion, font=("Arial", 16), bg="#B2EBF2", padx=20, pady=10)
   
    
    #crear_presupuesto_frame = tk.Frame(opciones_frame, bg="snow2")
    #crear_presupuesto_frame.grid(row=2, column=0, padx=20, pady=10)
    #tk.Label(crear_presupuesto_frame, text="Crear y agregar Presupuesto", font=("Arial", 12), bg="snow2", anchor="w").grid(row=0, column=0, sticky="w")
    #boton_presupuestos = tk.Button(crear_presupuesto_frame, text="Presupuesto", command=presupuestos.presupuesto, font=("Arial", 16), bg="#B2EBF2", padx=20, pady=10)
    #boton_presupuestos.grid(row=0, column=1, padx=10)

    
    #boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 16), bg="#FFC107", padx=20, pady=10)
    #boton_salir.pack(pady=20)

if __name__ == '__main__':
    ventana_root = tk.Tk()
    ventana_root.withdraw()
    mostrar_menu_tecnico(ventana_root)
    ventana_root.mainloop()