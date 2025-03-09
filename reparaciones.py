
import os


import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import consulta
import datetime 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import win32api



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

    # Datos del cliente (igual que antes)
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

    # Datos del celular (igual que antes)
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
            numero_orden = cursor.lastrowid  # Obtiene el número de orden generado automáticamente
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

            generar_pdf_orden(numero_orden)   #genera el PDF


            ventana_reparacion.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar la orden de reparación: {e}")


    boton_finalizar = tk.Button(ventana_reparacion, text="Guardar Orden", command=finalizar_reparacion)
    boton_finalizar.pack()

    
def consultar_reparacion():
    consulta.consultar_reparacion()

def generar_pdf_orden(numero_orden):    #funcion para generar el codigo 
    try:
        conexion = sqlite3.connect("reparaciones.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM reparaciones WHERE numero_orden = ?", (numero_orden,))
        orden = cursor.fetchone()
        conexion.close()

        if orden:
            nombre_archivo = f"orden_reparacion_{numero_orden}.pdf"
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            c.drawString(100, 750, f"Orden de Reparación #{numero_orden}")
            c.drawString(100, 730, f"Fecha de Ingreso: {orden[8]}")
            c.drawString(100, 710, f"Nombre y Apellido: {orden[1]}")
            c.drawString(100, 690, f"DNI: {orden[2]}")
            c.drawString(100, 670, f"Contacto: {orden[3]}")
            c.drawString(100, 650, f"Marca: {orden[4]}")
            c.drawString(100, 630, f"Modelo: {orden[5]}")
            c.drawString(100, 610, f"Falla: {orden[6]}")
            c.drawString(100, 590, f"Observaciones: {orden[7]}")
            c.save()

            if messagebox.askyesno("Imprimir", "¿Desea imprimir la orden de reparación?"):
                try:
                    ruta_absoluta = os.path.abspath(nombre_archivo)
                    win32api.ShellExecute(0, "print", ruta_absoluta, None, ".", 0)

                except win32api.error as e:
                    if e.winerror == 1155:
                        messagebox.showerror("Error", "No se encontró un visor de PDF asociado. Por favor, instale uno.")
                    else:
                        messagebox.showerror("Error", f"Error de impresión: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Error inesperado: {e}")
       
            else:
                messagebox.showerror("Error", "No se encontró la orden de reparación.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar o imprimir el PDF: {e}")



