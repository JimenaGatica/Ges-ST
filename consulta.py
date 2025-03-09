import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

def consultar_reparacion():
    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("Consultar Reparación")

    def buscar_por_numero_orden():
        ventana_buscar_orden = tk.Toplevel()
        ventana_buscar_orden.title("Buscar por Número de Orden")

        numero_orden_label = tk.Label(ventana_buscar_orden, text="Número de Orden:")
        numero_orden_label.pack()
        numero_orden_entry = tk.Entry(ventana_buscar_orden)
        numero_orden_entry.pack()

        def buscar():
            numero_orden = numero_orden_entry.get()
            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM reparaciones WHERE numero_orden = ?", (numero_orden,))
                resultado = cursor.fetchone()
                conexion.close()

                if resultado:
                    informacion = f"Número de Orden: {resultado[0]}\n" \
                                  f"Nombre y Apellido: {resultado[1]}\n" \
                                  f"DNI: {resultado[2]}\n" \
                                  f"Contacto: {resultado[3]}\n" \
                                  f"Marca: {resultado[4]}\n" \
                                  f"Modelo: {resultado[5]}\n" \
                                  f"Falla: {resultado[6]}\n" \
                                  f"Observaciones: {resultado[7]}\n" \
                                  f"Fecha de Ingreso: {resultado[8]}\n" \
                                  f"Estado de Reparación: {resultado[9]}\n" \
                                  f"Fecha de Estado: {resultado[10]}"

                    ventana_informacion = tk.Toplevel()
                    ventana_informacion.title("Información de la Reparación")
                    tk.Label(ventana_informacion, text=informacion).pack()

                    def modificar_estado():
                        menu_estado = tk.Menu(boton_estado, tearoff=0)
                        estados = ["EN REVISION", "A ESPERA DE REPUESTO", "REPARADO", "REPARADO Y RETIRADO", "RETIRADO SIN REPARAR"]

                        def actualizar_estado(nuevo_estado):
                            try:
                                conexion = sqlite3.connect("reparaciones.db")
                                cursor = conexion.cursor()
                                cursor.execute("UPDATE reparaciones SET estado_reparacion = ?, fecha_estado = ? WHERE numero_orden = ?", (nuevo_estado, datetime.datetime.now(), numero_orden))
                                conexion.commit()
                                conexion.close()
                                messagebox.showinfo("Estado Actualizado", "El estado de la reparación ha sido actualizado.")
                                ventana_informacion.destroy()
                            except sqlite3.Error as e:
                                messagebox.showerror("Error", f"Error al actualizar el estado: {e}")

                        for estado in estados:
                            menu_estado.add_command(label=estado, command=lambda e=estado: actualizar_estado(e))

                        boton_estado["menu"] = menu_estado

                    boton_estado = tk.Menubutton(ventana_informacion, text="Modificar Estado", relief=tk.RAISED)
                    boton_estado.pack()
                    modificar_estado()

                    def agregar_observacion():
                        ventana_agregar_observacion = tk.Toplevel()
                        ventana_agregar_observacion.title("Agregar Observación")

                        nueva_observacion_label = tk.Label(ventana_agregar_observacion, text="Nueva Observación:")
                        nueva_observacion_label.pack()
                        nueva_observacion_entry = tk.Entry(ventana_agregar_observacion)
                        nueva_observacion_entry.pack()

                        def guardar_observacion():
                            nueva_observacion = nueva_observacion_entry.get()
                            try:
                                conexion = sqlite3.connect("reparaciones.db")
                                cursor = conexion.cursor()
                                cursor.execute("UPDATE reparaciones SET observaciones = observaciones || ? WHERE numero_orden = ?", (f"\n{nueva_observacion}", numero_orden))
                                conexion.commit()
                                conexion.close()
                                messagebox.showinfo("Observación Agregada", "La observación ha sido agregada.")
                                ventana_agregar_observacion.destroy()
                                ventana_informacion.destroy()
                            except sqlite3.Error as e:
                                messagebox.showerror("Error", f"Error al agregar la observación: {e}")

                        boton_guardar_observacion = tk.Button(ventana_agregar_observacion, text="Guardar Observación", command=guardar_observacion)
                        boton_guardar_observacion.pack()

                    boton_agregar_observacion = tk.Button(ventana_informacion, text="Agregar Observación", command=agregar_observacion)
                    boton_agregar_observacion.pack()

                else:
                    messagebox.showinfo("Información", "No se encontró la reparación")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al buscar la reparación: {e}")

        boton_buscar = tk.Button(ventana_buscar_orden, text="Buscar", command=buscar)
        boton_buscar.pack()

    def buscar_por_dni():
        ventana_buscar_dni = tk.Toplevel()
        ventana_buscar_dni.title("Buscar por DNI")

        dni_label = tk.Label(ventana_buscar_dni, text="DNI:")
        dni_label.pack()
        dni_entry = tk.Entry(ventana_buscar_dni)
        dni_entry.pack()

        def buscar():
            dni = dni_entry.get()
            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM reparaciones WHERE dni = ?", (dni,))
                resultados = cursor.fetchall()
                conexion.close()

                if resultados:
                    for resultado in resultados:
                        informacion = f"Número de Orden: {resultado[0]}\n" \
                                      f"Nombre y Apellido: {resultado[1]}\n" \
                                      f"DNI: {resultado[2]}\n" \
                                      f"Contacto: {resultado[3]}\n" \
                                      f"Marca: {resultado[4]}\n" \
                                      f"Modelo: {resultado[5]}\n" \
                                      f"Falla: {resultado[6]}\n" \
                                      f"Observaciones: {resultado[7]}\n" \
                                      f"Fecha de Ingreso: {resultado[8]}\n" \
                                      f"Estado de Reparación: {resultado[9]}\n" \
                                      f"Fecha de Estado: {resultado[10]}\n\n"
                        messagebox.showinfo("Información de la Reparación", informacion)
                else:
                    messagebox.showinfo("Información", "No se encontró la reparación")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al buscar la reparación: {e}")

        boton_buscar = tk.Button(ventana_buscar_dni, text="Buscar", command=buscar)
        boton_buscar.pack()

    boton_buscar_orden = tk.Button(ventana_consultar, text="Buscar por Número de Orden", command=buscar_por_numero_orden)
    boton_buscar_orden.pack()

    boton_buscar_dni = tk.Button(ventana_consultar, text="Buscar por DNI", command=buscar_por_dni)
    boton_buscar_dni.pack()