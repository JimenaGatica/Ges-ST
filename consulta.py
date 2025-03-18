import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

def consultar_reparacion():
    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("Consultar Reparación")
    ventana_consultar.state('zoomed')
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
                    try:
                        fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M, %d/%m/%Y")
                    except ValueError:
                        # Si el formato sin microsegundos funciona (para registros antiguos)
                        fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")

                    informacion = f"Número de Orden: {resultado[0]}\n" \
                                  f"Nombre y Apellido: {resultado[1]}\n" \
                                  f"DNI: {resultado[2]}\n" \
                                  f"Contacto: {resultado[3]}\n" \
                                  f"Marca: {resultado[4]}\n" \
                                  f"Modelo: {resultado[5]}\n" \
                                  f"Falla: {resultado[6]}\n" \
                                  f"Observaciones: {resultado[7]}\n" \
                                  f"Fecha de Ingreso: {fecha_ingreso}\n" \
                                  f"Estado de Reparación: {resultado[9]}\n" \
                                  f"Fecha de Estado: {fecha_estado}"

                    ventana_informacion = tk.Toplevel()
                    ventana_informacion.title("Información de la Reparación")
                    ventana_informacion.geometry("600x600+50+50")
                    ventana_informacion.configure(bg="snow2")

                    texto_informacion = tk.Text(ventana_informacion, font=("Arial", 14), wrap=tk.WORD, bg="snow2")
                    texto_informacion.insert(tk.END, informacion)
                    texto_informacion.config(state=tk.DISABLED)
                    texto_informacion.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

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
                        try:
                            fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M, %d/%m/%Y")
                        except ValueError:
                            fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")

                        informacion += f"Número de Orden: {resultado[0]}\n" \
                                       f"Nombre y Apellido: {resultado[1]}\n" \
                                       f"DNI: {resultado[2]}\n" \
                                       f"Contacto: {resultado[3]}\n" \
                                       f"Marca: {resultado[4]}\n" \
                                       f"Modelo: {resultado[5]}\n" \
                                       f"Falla: {resultado[6]}\n" \
                                       f"Observaciones: {resultado[7]}\n" \
                                       f"Fecha de Ingreso: {fecha_ingreso}\n" \
                                       f"Estado de Reparación: {resultado[9]}\n" \
                                       f"Fecha de Estado: {fecha_estado}\n\n"

                    ventana_informacion = tk.Toplevel()
                    ventana_informacion.title("Información de la Reparación")
                    ventana_informacion.geometry("600x600+50+50")
                    ventana_informacion.configure(bg="snow2")

                    texto_informacion = tk.Text(ventana_informacion, font=("Arial", 14), wrap=tk.WORD, bg="snow2")
                    texto_informacion.insert(tk.END, informacion)
                    texto_informacion.config(state=tk.DISABLED)
                    texto_informacion.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

                else:
                    messagebox.showinfo("Información", "No se encontró la reparación")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al buscar la reparación: {e}")

        boton_buscar = tk.Button(ventana_buscar_dni, text="Buscar", command=buscar, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

    def ver_todo():
        try:
            conexion = sqlite3.connect("reparaciones.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM reparaciones")
            resultados = cursor.fetchall()
            conexion.close()

            ventana_ver_todo = tk.Toplevel()
            ventana_ver_todo.title("Todas las Reparaciones")
            ventana_ver_todo.geometry("900x600+50+0")
            ventana_ver_todo.configure(bg="snow2")

            texto_resultados = tk.Text(ventana_ver_todo, font=("Arial", 12), wrap=tk.WORD, bg="snow2")
            texto_resultados.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

            if resultados:
                for resultado in resultados:
                    fecha_ingreso = datetime.datetime.strptime(resultado[8], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")
                    try:
                        fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M, %d/%m/%Y")
                    except ValueError:
                        fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")

                    informacion = f"Número de Orden: {resultado[0]}\n" \
                                  f"Nombre y Apellido: {resultado[1]}\n" \
                                  f"DNI: {resultado[2]}\n" \
                                  f"Contacto: {resultado[3]}\n" \
                                  f"Marca: {resultado[4]}\n" \
                                  f"Modelo: {resultado[5]}\n" \
                                  f"Falla: {resultado[6]}\n" \
                                  f"Observaciones: {resultado[7]}\n" \
                                  f"Fecha de Ingreso: {fecha_ingreso}\n" \
                                  f"Estado de Reparación: {resultado[9]}\n" \
                                  f"Fecha de Estado: {fecha_estado}\n\n"
                    texto_resultados.insert(tk.END, informacion)
            else:
                messagebox.showinfo("Información", "No hay reparaciones registradas.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al consultar las reparaciones: {e}")

    def ver_solo():
        ventana_ver_solo = tk.Toplevel()
        ventana_ver_solo.title("Filtrar por Estado")
        ventana_ver_solo.geometry("500x400+200+100")
        ventana_ver_solo.configure(bg="snow2")

        estados_reparacion = ["INGRESADO", "EN REVISION", "A ESPERA DE REPUESTO", "REPARADO", "REPARADO Y RETIRADO", "RETIRADO SIN REPARAR"]
        selected_states = []

        def toggle_state(state):
            if state in selected_states:
                selected_states.remove(state)
            else:
                selected_states.append(state)

        def buscar_por_estados():
            if not selected_states:
                messagebox.showinfo("Información", "Por favor, seleccione al menos un estado.")
                return

            try:
                conexion = sqlite3.connect("reparaciones.db")
                cursor = conexion.cursor()
                placeholders = ','.join(['?'] * len(selected_states))
                cursor.execute(f"SELECT * FROM reparaciones WHERE estado_reparacion IN ({placeholders})", selected_states)
                resultados = cursor.fetchall()
                conexion.close()

                ventana_resultados_estados = tk.Toplevel()
                ventana_resultados_estados.title("Reparaciones por Estado")
                ventana_resultados_estados.geometry("900x600+0+0")
                ventana_resultados_estados.configure(bg="snow2")

                texto_resultados = tk.Text(ventana_resultados_estados, font=("Arial", 12), wrap=tk.WORD, bg="snow2")
                texto_resultados.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

                if resultados:
                    for resultado in resultados:
                        fecha_ingreso = datetime.datetime.strptime(resultado[8], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")
                        try:
                            fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%M, %d/%m/%Y")
                        except ValueError:
                            fecha_estado = datetime.datetime.strptime(resultado[10], "%Y-%m-%d %H:%M:%S").strftime("%H:%M, %d/%m/%Y")

                        informacion = f"Número de Orden: {resultado[0]}\n" \
                                      f"Nombre y Apellido: {resultado[1]}\n" \
                                      f"DNI: {resultado[2]}\n" \
                                      f"Contacto: {resultado[3]}\n" \
                                      f"Marca: {resultado[4]}\n" \
                                      f"Modelo: {resultado[5]}\n" \
                                      f"Falla: {resultado[6]}\n" \
                                      f"Observaciones: {resultado[7]}\n" \
                                      f"Fecha de Ingreso: {fecha_ingreso}\n" \
                                      f"Estado de Reparación: {resultado[9]}\n" \
                                      f"Fecha de Estado: {fecha_estado}\n\n"
                        texto_resultados.insert(tk.END, informacion)
                else:
                    messagebox.showinfo("Información", f"No se encontraron reparaciones con los estados seleccionados: {', '.join(selected_states)}")
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al consultar las reparaciones: {e}")

        check_vars = {}
        for i, estado in enumerate(estados_reparacion):
            var = tk.BooleanVar()
            check_vars[estado] = var
            chk = tk.Checkbutton(ventana_ver_solo, text=estado, variable=var, command=lambda s=estado: toggle_state(s), bg="snow2")
            chk.grid(row=i, column=0, sticky="w", padx=10, pady=5)

        btn_buscar = tk.Button(ventana_ver_solo, text="Buscar", command=buscar_por_estados, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        btn_buscar.place(relx=0.8, rely=0.4, anchor=tk.CENTER)


    bienvenidaconsulta_label = tk.Label(ventana_consultar, text="Bienvenido a la Gestión de consultas, usted podrá:", font=("Arial", 22, "bold"), bg="snow2")
    bienvenidaconsulta_label.pack(pady=20)

    # Opción 1: Buscar por numero de orden
    buscar_orden_label=tk.Label(ventana_consultar, text="Buscar orden dereparacion por Número de orden: ", font=("Arial", 18), bg="snow2")
    buscar_orden_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

    boton_buscar_orden = tk.Button(ventana_consultar, text="Buscar por Número de Orden", command=buscar_por_numero_orden, font=("Arial", 14), bg="#B2EBF2", padx=20, pady=10)
    boton_buscar_orden.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
    
    # Opción 2: Buscar por numero de DNI
    buscar_dni_label=tk.Label(ventana_consultar, text= "Buscar orden dereparacion por Número de DNI: ", font=("Arial", 18), bg="snow2")
    buscar_dni_label.place(relx=0.29, rely=0.45, anchor=tk.CENTER)

    boton_buscar_dni = tk.Button(ventana_consultar, text="Buscar por DNI", command=buscar_por_dni, font=("Arial", 14), bg="#B2EBF2", padx=20, pady=10)
    boton_buscar_dni.place(relx=0.8, rely=0.45, anchor=tk.CENTER)

    # Opción 3: Ver todas las ordenes de reparación
    buscar_ver_todo_label=tk.Label(ventana_consultar, text= "Ver todas las ordenes de Reparación: ", font=("Arial", 18), bg="snow2")
    buscar_ver_todo_label.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    boton_ver_todo = tk.Button(ventana_consultar, text="Ver Todo", command=ver_todo, font=("Arial", 14), bg="#B2EBF2", padx=20, pady=10)
    boton_ver_todo.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

    # Opción 4: Filtrado por estado de reparación
    buscar_ver_solo_label=tk.Label(ventana_consultar, text= "Filtrar las Ordenes de Reparación por estado: ", font=("Arial", 18), bg="snow2")
    buscar_ver_solo_label.place(relx=0.29, rely=0.8, anchor=tk.CENTER)

    boton_ver_solo = tk.Button(ventana_consultar, text="Ver Solo", command=ver_solo, font=("Arial", 14), bg="#B2EBF2", padx=20, pady=10)
    boton_ver_solo.place(relx=0.8, rely=0.8, anchor=tk.CENTER) # Ajustado para evitar superposición

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    ventana_principal.withdraw()  # Oculta la ventana principal
    consultar_reparacion()
    ventana_principal.mainloop()