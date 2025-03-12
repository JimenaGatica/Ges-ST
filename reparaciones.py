import tkinter as tk
from tkinter import messagebox
import sqlite3
import consulta

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
    ventana_reparacion.title("Nueva Orden de Reparación")

    # Datos del cliente
    tk.Label(ventana_reparacion, text="Datos del Cliente").pack()
    nombre_apellido_label = tk.Label(ventana_reparacion, text="Nombre y Apellido:")
    nombre_apellido_label.pack()
    nombre_apellido_entry = tk.Entry(ventana_reparacion)
    nombre_apellido_entry.pack()

    dni_label = tk.Label(ventana_reparacion, text="DNI:")
    dni_label.pack()
    dni_entry = tk.Entry(ventana_reparacion)
    dni_entry.pack()

    contacto_label = tk.Label(ventana_reparacion, text="Número de Contacto:")
    contacto_label.pack()
    contacto_entry = tk.Entry(ventana_reparacion)
    contacto_entry.pack()

    # Datos del celular
    tk.Label(ventana_reparacion, text="Datos del Celular").pack()
    marca_label = tk.Label(ventana_reparacion, text="Marca:")
    marca_label.pack()
    marca_entry = tk.Entry(ventana_reparacion)
    marca_entry.pack()

    modelo_label = tk.Label(ventana_reparacion, text="Modelo:")
    modelo_label.pack()
    modelo_entry = tk.Entry(ventana_reparacion)
    modelo_entry.pack()

    falla_label = tk.Label(ventana_reparacion, text="Falla:")
    falla_label.pack()
    falla_entry = tk.Entry(ventana_reparacion)
    falla_entry.pack()

    observaciones_label = tk.Label(ventana_reparacion, text="Observaciones:")
    observaciones_label.pack()
    observaciones_entry = tk.Entry(ventana_reparacion)
    observaciones_entry.pack()

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
            fecha_ingreso = resultado[0]
            conexion.close()

            informacion = f"Número de Orden: {numero_orden}\n" \
                          f"Fecha de Ingreso: {fecha_ingreso}\n" \
                          f"Datos del Cliente:\n" \
                          f"  Nombre y Apellido: {nombre_apellido}\n" \
                          f"  DNI: {dni}\n" \
                          f"  Número de Contacto: {contacto}\n" \
                          f"Datos del Celular:\n" \
                          f"  Marca: {marca}\n" \
                          f"  Modelo: {modelo}\n" \
                          f"  Falla: {falla}\n" \
                          f"  Observaciones: {observaciones}"

            messagebox.showinfo("Información de la Reparación", informacion)
            ventana_reparacion.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar la orden de reparación: {e}")

    boton_finalizar = tk.Button(ventana_reparacion, text="Guardar Orden", command=finalizar_reparacion)
    boton_finalizar.pack()

def consultar_reparacion():
    consulta.consultar_reparacion()

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Reparaciones")

boton_nueva_reparacion = tk.Button(ventana_principal, text="Nueva Reparación", command=nueva_reparacion)
boton_nueva_reparacion.pack()

boton_consultar_reparacion = tk.Button(ventana_principal, text="Consultar Reparación", command=consultar_reparacion)
boton_consultar_reparacion.pack()

ventana_principal.mainloop()

