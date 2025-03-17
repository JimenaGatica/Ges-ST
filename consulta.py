import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

def consultar_reparacion():
    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("Consultar Reparación")
    ventana_consultar.geometry("900x400+200+100")
    ventana_consultar.configure(bg="snow2")

    def buscar_por_numero_orden():
        ventana_buscar_orden = tk.Toplevel()
        ventana_buscar_orden.title("Buscar por Número de Orden")
        ventana_buscar_orden.geometry("900x400+200+100")
        ventana_buscar_orden.configure(bg="snow2")

        numero_orden_label = tk.Label(ventana_buscar_orden, text="Número de Orden:", font=("Arial", 16), bg="snow2")
        numero_orden_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        numero_orden_entry = tk.Entry(ventana_buscar_orden, width=40)
        numero_orden_entry.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

        def buscar():
            numero_orden = numero_orden_entry.get()
            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM reparaciones WHERE numero_orden = ?", (numero_orden,))
                resultado = cursor.fetchone()
                conexion.close()

                if resultado:

                    fecha_ingreso = datetime.datetime.strptime(resultado[8], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")
                    fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")


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
                    ventana_informacion.geometry("600x900")
                    ventana_informacion.configure(bg="snow2")

                    texto_informacion = tk.Text(ventana_informacion, font=("Arial", 14), wrap=tk.WORD, bg="snow2")
                    texto_informacion.insert(tk.END, informacion)
                    texto_informacion.config(state=tk.DISABLED)
                    texto_informacion.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

                    def modificar_estado_reparacion():
                        menu_estado = tk.Menu(boton_estado, tearoff=0)
                        estados = ["INGRESADO", "EN REVISION", "A ESPERA DE REPUESTO", "REPARADO", "REPARADO Y RETIRADO", "RETIRADO SIN REPARAR"]

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
                    boton_estado.place(relx=0.5, rely=0.80, anchor= tk.CENTER )
                    modificar_estado_reparacion()

                else:
                    messagebox.showinfo("Información", "No se encontró la reparación")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al buscar la reparación: {e}")

        boton_buscar = tk.Button(ventana_buscar_orden, text="Buscar", command=buscar, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

    def buscar_por_dni():
        ventana_buscar_dni = tk.Toplevel()
        ventana_buscar_dni.title("Buscar por DNI")
        ventana_buscar_dni.geometry("900x400+200+100")
        ventana_buscar_dni.configure(bg="snow2")

        dni_label = tk.Label(ventana_buscar_dni, text="DNI:", font=("Arial", 16), bg="snow2")
        dni_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        dni_entry = tk.Entry(ventana_buscar_dni, width=40)
        dni_entry.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

        def buscar():
            dni = dni_entry.get()
            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM reparaciones WHERE dni = ?", (dni,))
                resultados = cursor.fetchall()
                conexion.close()

                if resultados:
                    informacion = ""
                    for resultado in resultados:

                        fecha_ingreso = datetime.datetime.strptime(resultado[8], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")
                        fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")

                        informacion += f"Número de Orden: {resultado[0]}\n" \
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

                    ventana_informacion = tk.Toplevel()
                    ventana_informacion.title("Información de la Reparación")
                    ventana_informacion.geometry("600x900")
                    ventana_informacion.configure(bg="snow2")

                    texto_informacion = tk.Text(ventana_informacion, font=("Arial", 14), wrap=tk.WORD, bg="snow2")
                    texto_informacion.insert(tk.END, informacion)
                    texto_informacion.config(state=tk.DISABLED)
                    texto_informacion.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

                    def modificar_estado_reparacion():
                        menu_estado = tk.Menu(boton_estado, tearoff=0)
                        estados = ["INGRESADO", "EN REVISION", "A ESPERA DE REPUESTO", "REPARADO", "REPARADO Y RETIRADO", "RETIRADO SIN REPARAR"]

                        def actualizar_estado(nuevo_estado):
                            try:
                                conexion = sqlite3.connect("reparaciones.db")
                                cursor = conexion.cursor()
                                cursor.execute("UPDATE reparaciones SET estado_reparacion = ?, fecha_estado = ? WHERE numero_orden = ?", (nuevo_estado, datetime.datetime.now(), resultado[0]))
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
                    modificar_estado_reparacion()

                else:
                    messagebox.showinfo("Información", "No se encontró la reparación")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al buscar la reparación: {e}")

        boton_buscar = tk.Button(ventana_buscar_dni, text="Buscar", command=buscar, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

    boton_buscar_orden = tk.Button(ventana_consultar, text="Buscar por Número de Orden", command=buscar_por_numero_orden, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_buscar_orden.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

    boton_buscar_dni = tk.Button(ventana_consultar, text="Buscar por DNI", command=buscar_por_dni, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_buscar_dni.place(relx=0.7, rely=0.5, anchor=tk.CENTER)