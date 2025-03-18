import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

def modificar_estado():
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Modificar Estado de Reparación")
    ventana_modificar.geometry("900x400+200+100")
    ventana_modificar.configure(bg="snow2")

    

    numero_orden_label = tk.Label(ventana_modificar, text="Ingrese número de orden:", font=("Arial", 16), bg="snow2")
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
                ventana_info.geometry("700x500+100+50")
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
                            ventana_modificar.destroy()
                        except sqlite3.Error as e:
                            messagebox.showerror("Error", f"Error al actualizar el estado: {e}")

                    for estado in estados:
                        menu_estado.add_command(label=estado, command=lambda e=estado: actualizar_estado(e))

                    boton_estado["menu"] = menu_estado

                boton_estado = tk.Menubutton(ventana_info, text="Modificar Estado",font=("Arial", 16), relief=tk.RAISED)
                boton_estado.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
                modificar_estado_reparacion()

            else:
                messagebox.showinfo("Reparación no encontrada", "No se encontró ninguna reparación con el número de orden ingresado.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al consultar la reparación: {e}")

    boton_buscar = tk.Button(ventana_modificar, text="Buscar", command=buscar_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_buscar.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("Gestión de Estados de Reparación")
    ventana_principal.geometry("400x200+200+100")
    ventana_principal.configure(bg="snow2")

    ventana_principal.mainloop()