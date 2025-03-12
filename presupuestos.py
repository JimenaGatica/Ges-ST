import tkinter as tk
from tkinter import messagebox
import sqlite3

def presupuesto():
    ventana_presupuesto = tk.Toplevel()
    ventana_presupuesto.title("Generar Presupuesto - Sistema de Gestión")
    ventana_presupuesto.geometry("900x400+200+100")
    ventana_presupuesto.configure(bg="snow2")

    def calcular_presupuesto():
        ventana_calcular = tk.Toplevel()
        ventana_calcular.title("Calcular Presupuesto")
        ventana_calcular.geometry("900x400+200+100")
        ventana_calcular.configure(bg="snow2")

        valor_repuesto_label = tk.Label(ventana_calcular, text="Valor del Repuesto:", font=("Arial", 16), bg="snow2")
        valor_repuesto_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        valor_repuesto_entry = tk.Entry(ventana_calcular, width=40)
        valor_repuesto_entry.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

        def calcular():
            try:
                valor_repuesto = float(valor_repuesto_entry.get())
                valor_envio = 8000
                valor_templado = 3000
                costo_repuesto = valor_repuesto + valor_envio + valor_templado
                valor_pago_anticipado = costo_repuesto * 2
                valor_pago_total = valor_pago_anticipado / 0.80

                resultado = f"Costo del Repuesto: {costo_repuesto}\n" \
                            f"Pago Anticipado: {valor_pago_anticipado}\n" \
                            f"Pago Total: {valor_pago_total}"
                messagebox.showinfo("Resultado", resultado)

                def agregar_a_reparacion():
                    ventana_agregar_reparacion = tk.Toplevel()
                    ventana_agregar_reparacion.title("Agregar a Reparación")
                    ventana_agregar_reparacion.geometry("900x400+200+100")
                    ventana_agregar_reparacion.configure(bg="snow2")

                    numero_orden_label = tk.Label(ventana_agregar_reparacion, text="Número de Orden:", bg="snow2")
                    numero_orden_label.grid(row=0, column=0, padx=10, pady=5)
                    numero_orden_entry = tk.Entry(ventana_agregar_reparacion)
                    numero_orden_entry.grid(row=0, column=1, padx=10, pady=5)

                    def agregar():
                        numero_orden = numero_orden_entry.get()
                        try:
                            conexion = sqlite3.connect("reparaciones.db")
                            cursor = conexion.cursor()
                            cursor.execute("UPDATE reparaciones SET observaciones = observaciones || ? WHERE numero_orden = ?", (f"\nPresupuesto: {costo_repuesto}, Pago anticipado: {valor_pago_anticipado}, Pago total: {valor_pago_total}", numero_orden))
                            conexion.commit()
                            conexion.close()
                            messagebox.showinfo("Presupuesto Agregado", "El presupuesto ha sido agregado a la orden de reparación.")
                            ventana_agregar_reparacion.destroy()
                        except sqlite3.Error as e:
                            messagebox.showerror("Error", f"Error al agregar el presupuesto: {e}")

                    boton_agregar = tk.Button(ventana_agregar_reparacion, text="Agregar", command=agregar)
                    boton_agregar.grid(row=1, column=0, columnspan=2, pady=10)

                boton_agregar_reparacion = tk.Button(ventana_calcular, text="Agregar a Reparación", command=agregar_a_reparacion, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
                boton_agregar_reparacion.grid(row=2, column=0, columnspan=2, pady=10)

            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numérico válido")

        boton_calcular = tk.Button(ventana_calcular, text="Calcular", command=calcular, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        boton_calcular.place(relx=0.5, rely=0.70, anchor=tk.CENTER)



    def agregar_presupuesto_personalizado():
        ventana_personalizado = tk.Toplevel()
        ventana_personalizado.title("Presupuesto Personalizado")
        ventana_personalizado.geometry("900x400+200+100")
        ventana_personalizado.configure(bg="snow2")

        pago_anticipado_label = tk.Label(ventana_personalizado, text="Pago Anticipado:", bg="snow2")
        pago_anticipado_label.grid(row=0, column=0, padx=10, pady=5)
        pago_anticipado_entry = tk.Entry(ventana_personalizado)
        pago_anticipado_entry.grid(row=0, column=1, padx=10, pady=5)

        def calcular_personalizado():
            try:
                pago_anticipado = float(pago_anticipado_entry.get())
                pago_total = pago_anticipado / 0.80

                resultado = f"Pago Anticipado: {pago_anticipado}\n" \
                            f"Pago Total: {pago_total}"
                messagebox.showinfo("Resultado", resultado)

                def agregar_a_reparacion():
                    ventana_agregar_reparacion = tk.Toplevel()
                    ventana_agregar_reparacion.title("Agregar a Reparación")
                    ventana_agregar_reparacion.geometry("900x400+200+100")
                    ventana_agregar_reparacion.configure(bg="snow2")

                    numero_orden_label = tk.Label(ventana_agregar_reparacion, text="Número de Orden:", bg="snow2")
                    numero_orden_label.grid(row=0, column=0, padx=10, pady=5)
                    numero_orden_entry = tk.Entry(ventana_agregar_reparacion)
                    numero_orden_entry.grid(row=0, column=1, padx=10, pady=5)

                    def agregar():
                        numero_orden = numero_orden_entry.get()
                        try:
                            conexion = sqlite3.connect("reparaciones.db")
                            cursor = conexion.cursor()
                            cursor.execute("UPDATE reparaciones SET observaciones = observaciones || ? WHERE numero_orden = ?", (f"\nPresupuesto Personalizado: Pago anticipado: {pago_anticipado}, Pago total: {pago_total}", numero_orden))
                            conexion.commit()
                            conexion.close()
                            messagebox.showinfo("Presupuesto Agregado", "El presupuesto ha sido agregado a la orden de reparación.")
                            ventana_agregar_reparacion.destroy()
                        except sqlite3.Error as e:
                            messagebox.showerror("Error", f"Error al agregar el presupuesto: {e}")

                    boton_agregar = tk.Button(ventana_agregar_reparacion, text="Agregar", command=agregar)
                    boton_agregar.grid(row=1, column=0, columnspan=2, pady=10)

                boton_agregar_reparacion = tk.Button(ventana_personalizado, text="Agregar a Reparación", command=agregar_a_reparacion)
                boton_agregar_reparacion.grid(row=2, column=0, columnspan=2, pady=10)

            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numérico válido")

        boton_calcular_personalizado = tk.Button(ventana_personalizado, text="Calcular", command=calcular_personalizado,  font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
        boton_calcular_personalizado.grid(row=1, column=0, columnspan=2, pady=10)

    boton_calcular_presupuesto = tk.Button(ventana_presupuesto, text="Calcular Presupuesto", command=calcular_presupuesto, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_calcular_presupuesto.place(relx=0.3, rely=0.45, anchor=tk.CENTER)


    boton_presupuesto_personalizado = tk.Button(ventana_presupuesto, text="Agregar Presupuesto Personalizado", command=agregar_presupuesto_personalizado, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_presupuesto_personalizado.place(relx=0.7, rely=0.45, anchor=tk.CENTER)