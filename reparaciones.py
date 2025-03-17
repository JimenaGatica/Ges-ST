import tkinter as tk
from tkinter import messagebox
import sqlite3
import consulta
import datetime

def crear_tabla_reparaciones():
    try:
        conexion = sqlite3.connect("reparaciones.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reparaciones (
                numero_orden INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_apellido TEXT,
                dni TEXT,
                contacto TEXT,
                marca TEXT,
                modelo TEXT,
                falla TEXT,
                observaciones TEXT,
                fecha_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado_reparacion TEXT DEFAULT 'INGRESADO',
                fecha_estado DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al crear la tabla de reparaciones: {e}")

crear_tabla_reparaciones()

def nueva_reparacion():
    ventana_reparacion = tk.Toplevel()
    ventana_reparacion.title("Nueva Orden de Reparación - Sistema de Gestión")
    ventana_reparacion.geometry("800x500+200+100")
    ventana_reparacion.configure(bg="snow2")  # Color de fondo

    # Datos del cliente
    tk.Label(ventana_reparacion, text="Datos del Cliente", font=("Arial", 12, "bold"), bg="snow2").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(ventana_reparacion, text="Nombre y Apellido:", font=("Arial", 12), bg="snow2").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    nombre_apellido_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    nombre_apellido_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana_reparacion, text="DNI:", font=("Arial", 12), bg="snow2").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    dni_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    dni_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana_reparacion, text="Número de Contacto:", font=("Arial", 12), bg="snow2").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    contacto_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    contacto_entry.grid(row=3, column=1, padx=10, pady=5)

    # Datos del celular
    tk.Label(ventana_reparacion, text="Datos del Celular", font=("Arial", 12, "bold"), bg="snow2").grid(row=4, column=0, columnspan=2, pady=10)
    tk.Label(ventana_reparacion, text="Marca:", font=("Arial", 12), bg="snow2").grid(row=5, column=0, sticky="w", padx=10, pady=5)
    marca_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    marca_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana_reparacion, text="Modelo:", font=("Arial", 12), bg="snow2").grid(row=6, column=0, sticky="w", padx=10, pady=5)
    modelo_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    modelo_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(ventana_reparacion, text="Falla:", font=("Arial", 12), bg="snow2").grid(row=7, column=0, sticky="w", padx=10, pady=5)
    falla_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    falla_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(ventana_reparacion, text="Observaciones:", font=("Arial", 12), bg="snow2").grid(row=8, column=0, sticky="w", padx=10, pady=5)
    observaciones_entry = tk.Entry(ventana_reparacion, font=("Arial", 12), width=40)  # Ancho aumentado a 40
    observaciones_entry.grid(row=8, column=1, padx=10, pady=5)

    def finalizar_reparacion():
        nombre_apellido = nombre_apellido_entry.get()
        dni = dni_entry.get()
        contacto = contacto_entry.get()
        marca = marca_entry.get()
        modelo = modelo_entry.get()
        falla = falla_entry.get()
        observaciones = observaciones_entry.get()

        try:
            conexion = sqlite3.connect("reparaciones.db")
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO reparaciones (nombre_apellido, dni, contacto, marca, modelo, falla, observaciones)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nombre_apellido, dni, contacto, marca, modelo, falla, observaciones))
            conexion.commit()
            numero_orden = cursor.lastrowid
            conexion.close()

            conexion = sqlite3.connect("reparaciones.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT fecha_ingreso FROM reparaciones WHERE numero_orden = ?", (numero_orden,))
            resultado = cursor.fetchone()
            fecha_ingreso_db = datetime.datetime.strptime(resultado[0], "%Y-%m-%d %H:%M:%S")
            fecha_ingreso_formateada = fecha_ingreso_db.strftime("%H:%M %d %m %Y")
            
            conexion.close()

            informacion = f"Número de Orden: {numero_orden}\n" \
                          f"Fecha de Ingreso: {fecha_ingreso_formateada}\n" \
                          f"Datos del Cliente:\n" \
                          f"  Nombre y Apellido: {nombre_apellido}\n" \
                          f"  DNI: {dni}\n" \
                          f"  Número de Contacto: {contacto}\n" \
                          f"Datos del Celular:\n" \
                          f"  Marca: {marca}\n" \
                          f"  Modelo: {modelo}\n" \
                          f"  Falla: {falla}\n" \
                          f"  Observaciones: {observaciones}"
            
            

            # Crear una nueva ventana para mostrar la información
            ventana_info = tk.Toplevel()
            ventana_info.title("Información de la Reparación")
            ventana_info.geometry("700x600+100+50")  # Tamaño de la ventana aumentado
            ventana_info.configure(bg="snow2") #color de fondo

            

            # Crear un widget Text para mostrar la información con formato
            texto_info = tk.Text(ventana_info, font=("Arial", 14), wrap=tk.WORD, bg="snow2") #fuente mas grande y color de fondo
            texto_info.insert(tk.END, informacion)
            texto_info.config(state=tk.DISABLED)  # Hacer que el texto sea de solo lectura
            texto_info.pack(padx=20, pady=20, fill=tk.BOTH, expand=True) #padding y expandir el texto

            def cerrar_ventanas():
                ventana_info.destroy()
                ventana_reparacion.destroy()
                

            boton_salir_info = tk.Button(ventana_info, text="Salir", command=cerrar_ventanas, font=("Arial", 16), bg="#FFC107")
            boton_salir_info.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


            ventana_reparacion.destroy()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar la orden de reparación: {e}")

    boton_finalizar = tk.Button (ventana_reparacion, text="Guardar Orden", command=finalizar_reparacion, font=("Arial", 12), bg="#B2EBF2")
    boton_finalizar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def consultar_reparacion():
    consulta.consultar_reparacion()

if __name__ == "__main__": #agrega esta proteccion.
    # Ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Gestión de Reparaciones")

    boton_nueva_reparacion = tk.Button(ventana_principal, text="Nueva Reparación", command=nueva_reparacion)
    boton_nueva_reparacion.pack()

    boton_consultar_reparacion = tk.Button(ventana_principal, text="Consultar Reparación", command=consultar_reparacion)
    boton_consultar_reparacion.pack()

    ventana_principal.mainloop()