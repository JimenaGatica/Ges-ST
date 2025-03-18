import tkinter as tk
from tkinter import messagebox
import presupuestos
import consulta
import estado
import datetime
import sqlite3

def mostrar_menu_tecnico(ventana_inicio, nombre_usuario):
    ventana_menu = tk.Toplevel()
    ventana_menu.title("Menú Técnico - Sistema de Gestión")
    ventana_menu.state('zoomed')
    ventana_menu.configure(bg="snow2")

    def volver_a_inicio():
        ventana_menu.destroy()
        ventana_inicio.deiconify()

    def agregar_observaciones():
        ventana_agregar_obs = tk.Toplevel()
        ventana_agregar_obs.title("Agregar Observaciones")
        ventana_agregar_obs.state('zoomed')
        ventana_agregar_obs.configure(bg="snow2")

        num_orden_label = tk.Label(ventana_agregar_obs, text="Número de Reparación:", font=("Arial", 14), bg="snow2")
        num_orden_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        num_orden_entry = tk.Entry(ventana_agregar_obs, width=30)
        num_orden_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        info_label = tk.Label(ventana_agregar_obs,
                             text="En esta área usted podrá agregar información adicional a la orden de reparación como falla encontrada, reparación realizada, proveedor y técnico que realizó la reparación.",
                             font=("Arial", 14), bg="snow2", wraplength=500)
        info_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        observaciones_label = tk.Label(ventana_agregar_obs, text="Observaciones:", font=("Arial", 14), bg="snow2")
        observaciones_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        observaciones_text = tk.Text(ventana_agregar_obs, width=60, height=10, font=("Arial", 14))
        observaciones_text.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        def guardar_observaciones():
            num_orden = num_orden_entry.get()
            observacion = observaciones_text.get("1.0", tk.END).strip()
            fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
            nombre_tecnico = nombre_usuario  # Obtener el nombre de usuario
            nueva_observacion = f"Nuevas observaciones: [{fecha_actual}] {observacion} - Técnico: {nombre_tecnico}"

            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT observaciones FROM reparaciones WHERE numero_orden = ?", (num_orden,))
                resultado = cursor.fetchone()

                if resultado:
                    observaciones_actuales = resultado[0] if resultado[0] else ""
                    observaciones_actuales += "\n" + nueva_observacion  # Agregar un salto de línea antes de la nueva observación
                    cursor.execute("UPDATE reparaciones SET observaciones = ? WHERE numero_orden = ?", (observaciones_actuales, num_orden))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("Observaciones Guardadas", "Las observaciones han sido agregadas a la orden de reparación.")
                    ventana_agregar_obs.destroy()
                else:
                    conexion.close()
                    messagebox.showerror("Error", "No se encontró la orden de reparación con ese número.")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al guardar las observaciones: {e}")

        guardar_button = tk.Button(ventana_agregar_obs, text="Guardar", command=guardar_observaciones, font=("Arial", 12), bg="#4CAF50", fg="white")
        guardar_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    # Título principal
    bienvenidatecnico_label = tk.Label(ventana_menu, text=f"Bienvenido a la Gestión Técnica, {nombre_usuario}", font=("Arial", 22, "bold"), bg="snow2")
    bienvenidatecnico_label.pack(pady=20)

    # Subtítulo
    operaciones_label = tk.Label(ventana_menu, text="Usted como técnico podrá realizar las siguientes operaciones:", font=("Arial", 18), bg="snow2")
    operaciones_label.pack(pady=10)

    # Opción 1: Modificar estado
    modificar_estado_label = tk.Label(ventana_menu, text="Modificar el estado de la Reparación", font=("Arial", 16), bg="snow2")
    modificar_estado_label.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

    boton_estado_reparacion = tk.Button(ventana_menu, text="Modificar Estado", command=estado.modificar_estado, font=("Arial", 16), bg="#B2EBF2")
    boton_estado_reparacion.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

    # Opción 2: Consultar reparación
    consultar_reparacio_label = tk.Label(ventana_menu, text="Ver toda la información de la Orden de Reparación", font=("Arial", 16), bg="snow2")
    consultar_reparacio_label.place(relx=0.25, rely=0.45, anchor=tk.CENTER)

    boton_consultar_reparacion = tk.Button(ventana_menu, text="Ver Orden de Reparación", command=consulta.consultar_reparacion, font=("Arial", 16), bg="#B2EBF2")
    boton_consultar_reparacion.place(relx=0.7, rely=0.45, anchor=tk.CENTER)

    # Opción 3: Crear presupuesto
    crear_presupuesto_label = tk.Label(ventana_menu, text="Crear y agregar Presupuesto a Ordenes de Reparación", font=("Arial", 16), bg="snow2")
    crear_presupuesto_label.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    boton_presupuesto = tk.Button(ventana_menu, text="Presupuesto", command=presupuestos.presupuesto, font=("Arial", 16), bg="#B2EBF2")
    boton_presupuesto.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

    # Nueva Opción: Agregar observaciones
    agregar_observaciones_label = tk.Label(ventana_menu, text="Agregar observaciones a una Orden de Reparación", font=("Arial", 16), bg="snow2")
    agregar_observaciones_label.place(relx=0.25, rely=0.75, anchor=tk.CENTER)

    boton_agregar_observaciones = tk.Button(ventana_menu, text="Agregar", command=agregar_observaciones, font=("Arial", 16), bg="#B2EBF2")
    boton_agregar_observaciones.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

    # Botón Salir
    boton_salir = tk.Button(ventana_menu, text="Salir", command=volver_a_inicio, font=("Arial", 16), bg="#FFC107", padx=20, pady=10)
    boton_salir.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

if __name__ == '__main__':
    ventana_root = tk.Tk()
    ventana_root.withdraw()
    # Para probar, puedes simular un nombre de usuario aquí
    mostrar_menu_tecnico(ventana_root, "UsuarioDePrueba")
    ventana_root.mainloop()