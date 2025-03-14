import tkinter as tk  
from tkinter import messagebox  
import sqlite3  
import datetime  

def modificar_estado():  
    ventana_modificar = tk.Toplevel()  
    ventana_modificar.title("Modificar Estado de Reparación")  
    ventana_modificar.geometry("900x400+200+100")  
    ventana_modificar.configure(bg="snow2")  

    numero_orden_label = tk.Label(ventana_modificar, text="Número de Orden:", font=("Arial", 16), bg="snow2")  
    numero_orden_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)  
    numero_orden_entry = tk.Entry(ventana_modificar, width=40)  
    numero_orden_entry.place(relx=0.5, rely=0.50, anchor=tk.CENTER)  

    def buscar_reparacion():  
        numero_orden = numero_orden_entry.get()  
        try:  
            conexion = sqlite3.connect("reparaciones.db")  
            cursor = conexion.cursor()  
            cursor.execute("SELECT * FROM reparaciones WHERE numero_orden = ?", (numero_orden,))  
            reparacion = cursor.fetchone()  
            conexion.close()  

            if reparacion:  
                informacion = f"Número de Orden: {reparacion[0]}\n" \
                              f"Nombre y Apellido: {reparacion[1]}\n" \
                              f"DNI: {reparacion[2]}\n" \
                              f"Contacto: {reparacion[3]}\n" \
                              f"Marca: {reparacion[4]}\n" \
                              f"Modelo: {reparacion[5]}\n" \
                              f"Falla: {reparacion[6]}\n" \
                              f"Observaciones: {reparacion[7]}\n" \
                              f"Fecha de Ingreso: {reparacion[8]}\n" \
                              f"Estado de Reparación: {reparacion[9]}\n" \
                              f"Fecha de Estado: {reparacion[10]}"  

                ventana_info = tk.Toplevel()  
                ventana_info.title("Información de la Reparación")  
                ventana_info.geometry("600x400")  
                ventana_info.configure(bg="snow2")  

                texto_info = tk.Text(ventana_info, font=("Arial", 14), wrap=tk.WORD, bg="snow2")  
                texto_info.insert(tk.END, informacion)  
                texto_info.config(state=tk.DISABLED)  
                texto_info.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  

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
                            ventana_info.destroy()  
                        except sqlite3.Error as e:  
                            messagebox.showerror("Error", f"Error al actualizar el estado: {e}")  

                    for estado in estados:  
                        menu_estado.add_command(label=estado, command=lambda e=estado: actualizar_estado(e))  

                    boton_estado["menu"] = menu_estado  

                boton_estado = tk.Menubutton(ventana_info, text="Modificar Estado", relief=tk.RAISED)  
                boton_estado.pack()  
                modificar_estado_reparacion()  

            else:  
                messagebox.showinfo("Reparación no encontrada", "No se encontró ninguna reparación con el número de orden ingresado.")  
        except sqlite3.Error as e:  
            messagebox.showerror("Error", f"Error al consultar la reparación: {e}")  

    boton_buscar = tk.Button(ventana_modificar, text="Buscar", command=buscar_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)  

def ver_reparaciones():  
    ventana_ver = tk.Toplevel()  
    ventana_ver.title("Ver Reparaciones")  
    ventana_ver.geometry("900x600+200+100")  
    ventana_ver.configure(bg="snow2")  

    # Crear el área de texto para mostrar los resultados  
    texto_resultados = tk.Text(ventana_ver, font=("Arial", 12), wrap=tk.WORD, bg="snow2")  
    texto_resultados.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  

    def ver_todo():  
        try:  
            conexion = sqlite3.connect("reparaciones.db")  
            cursor = conexion.cursor()  
            cursor.execute("SELECT numero_orden, marca, modelo, falla, estado_reparacion FROM reparaciones")  
            resultados = cursor.fetchall()  
            conexion.close()  

            # Limpiar el área de resultados antes de insertar nuevos  
            texto_resultados.delete(1.0, tk.END)  
            
            if resultados:  
                for resultado in resultados:  
                    texto_resultados.insert(tk.END, f"Número de Orden: {resultado[0]}, Marca: {resultado[1]}, Modelo: {resultado[2]}, Falla: {resultado[3]}, Estado: {resultado[4]}\n")  
            else:  
                messagebox.showinfo("Información", "No hay reparaciones registradas.")  
        except sqlite3.Error as e:  
            messagebox.showerror("Error", f"Error al consultar las reparaciones: {e}")  

    def ver_por_estado(estado_seleccionado):  
        try:  
            conexion = sqlite3.connect("reparaciones.db")  
            cursor = conexion.cursor()  
            cursor.execute("SELECT numero_orden, marca, modelo, falla, estado_reparacion FROM reparaciones WHERE estado_reparacion = ?", (estado_seleccionado,))  
            resultados = cursor.fetchall()  
            conexion.close()  

            # Limpiar el área de resultados antes de insertar nuevos  
            texto_resultados.delete(1.0, tk.END)  
            
            if resultados:  
                for resultado in resultados:  
                    texto_resultados.insert(tk.END, f"Número de Orden: {resultado[0]}, Marca: {resultado[1]}, Modelo: {resultado[2]}, Falla: {resultado[3]}, Estado: {resultado[4]}\n")  
            else:  
                messagebox.showinfo("Información", f"No hay reparaciones con el estado '{estado_seleccionado}'.")  
        except sqlite3.Error as e:  
            messagebox.showerror("Error", f"Error al consultar las reparaciones: {e}")  

    boton_ver_todo = tk.Button(ventana_ver, text="Ver Todo", command=ver_todo, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_ver_todo.pack(pady=10)  

    # Crear el menú desplegable "Ver Solo"  
    menu_estados = tk.Menu(ventana_ver, tearoff=0)  
    estados = ["INGRESADO", "EN REVISION", "A ESPERA DE REPUESTO", "REPARADO", "REPARADO Y RETIRADO", "RETIRADO SIN REPARAR"]  
    for estado in estados:  
        menu_estados.add_command(label=estado, command=lambda e=estado: ver_por_estado(e))  

    # Crear el botón "Ver Solo" que despliega el menú  
    #boton_ver_solo = tk.Menubutton(ventana_ver, text="Ver Solo", relief=tk.RAISED)  
    #boton_ver_solo["menu"] = menu_estados  
    #boton_ver_solo.pack(pady=10)  

def gestion_estados():  
    ventana_gestion = tk.Toplevel()  
    ventana_gestion.title("Gestión de Estados")  
    ventana_gestion.geometry("400x200+200+100")  
    ventana_gestion.configure(bg="snow2")  

    boton_modificar = tk.Button(ventana_gestion, text="Modificar Estado", command=modificar_estado, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_modificar.pack(pady=10)  

    boton_ver = tk.Button(ventana_gestion, text="Ver", command=ver_reparaciones, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_ver.pack(pady=10)  

def ver_reparacion():  
    ventana_buscar = tk.Toplevel()  
    ventana_buscar.title("Buscar Reparación")  
    ventana_buscar.geometry("400x200+200+100")  
    ventana_buscar.configure(bg="snow2")  

    numero_orden_label = tk.Label(ventana_buscar, text="Número de Orden:", font=("Arial", 16), bg="snow2")  
    numero_orden_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)  
    numero_orden_entry = tk.Entry(ventana_buscar, width=40)  
    numero_orden_entry.place(relx=0.5, rely=0.50, anchor=tk.CENTER)  

    def buscar():  
        numero_orden = numero_orden_entry.get()  
        try:  
            conexion = sqlite3.connect("reparaciones.db")  
            cursor = conexion.cursor()  
            cursor.execute("SELECT * FROM reparaciones WHERE numero_orden = ?", (numero_orden,))  
            reparacion = cursor.fetchone()  
            conexion.close()  

            if reparacion:  
                informacion = f"Número de Orden: {reparacion[0]}\n" \
                              f"Nombre y Apellido: {reparacion[1]}\n" \
                              f"DNI: {reparacion[2]}\n" \
                              f"Contacto: {reparacion[3]}\n" \
                              f"Marca: {reparacion[4]}\n" \
                              f"Modelo: {reparacion[5]}\n" \
                              f"Falla: {reparacion[6]}\n" \
                              f"Observaciones: {reparacion[7]}\n" \
                              f"Fecha de Ingreso: {reparacion[8]}\n" \
                              f"Estado de Reparación: {reparacion[9]}\n" \
                              f"Fecha de Estado: {reparacion[10]}"  

                ventana_info = tk.Toplevel()  
                ventana_info.title("Información de la Reparación")  
                ventana_info.geometry("600x400")  
                ventana_info.configure(bg="snow2")  

                texto_info = tk.Text(ventana_info, font=("Arial", 14), wrap=tk.WORD, bg="snow2")  
                texto_info.insert(tk.END, informacion)  
                texto_info.config(state=tk.DISABLED)  
                texto_info.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  
            else:  
                messagebox.showinfo("Reparación no encontrada", "No se encontró ninguna reparación con el número de orden ingresado.")  
        except sqlite3.Error as e:  
            messagebox.showerror("Error", f"Error al consultar la reparación: {e}")  

    boton_buscar = tk.Button(ventana_buscar, text="Buscar", command=buscar, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)  

if __name__ == "__main__":  
    ventana_principal = tk.Tk()  
    ventana_principal.title("Gestión de Estados de Reparación")  
    ventana_principal.geometry("400x200+200+100")  
    ventana_principal.configure(bg="snow2")  

    boton_modificar = tk.Button(ventana_principal, text="Modificar Estado", command=gestion_estados, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_modificar.pack(pady=20)  

    boton_ver = tk.Button(ventana_principal, text="Ver", command=ver_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)  
    boton_ver.pack(pady=20)  

    ventana_principal.mainloop()  