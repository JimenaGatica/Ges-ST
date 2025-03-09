import tkinter as tk
from tkinter import messagebox
import sqlite3

def presupuesto():
    ventana_presupuesto = tk.Toplevel()
    ventana_presupuesto.title("Presupuesto")

    def calcular_presupuesto():
        ventana_calcular = tk.Toplevel()
        ventana_calcular.title("Calcular Presupuesto")

        valor_repuesto_label = tk.Label(ventana_calcular, text="Valor del Repuesto:")
        valor_repuesto_label.pack()
        valor_repuesto_entry = tk.Entry(ventana_calcular)
        valor_repuesto_entry.pack()

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

                    numero_orden_label = tk.Label(ventana_agregar_reparacion, text="Número de Orden:")
                    numero_orden_label.pack()
                    numero_orden_entry = tk.Entry(ventana_agregar_reparacion)
                    numero_orden_entry.pack()

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
                    boton_agregar.pack()

                boton_agregar_reparacion = tk.Button(ventana_calcular, text="Agregar a Reparación", command=agregar_a_reparacion)
                boton_agregar_reparacion.pack()

            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numérico válido")

        boton_calcular = tk.Button(ventana_calcular, text="Calcular", command=calcular)
        boton_calcular.pack()

    def agregar_presupuesto_personalizado():
        ventana_personalizado = tk.Toplevel()
        ventana_personalizado.title("Presupuesto Personalizado")

        pago_anticipado_label = tk.Label(ventana_personalizado, text="Pago Anticipado:")
        pago_anticipado_label.pack()
        pago_anticipado_entry = tk.Entry(ventana_personalizado)
        pago_anticipado_entry.pack()

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

                    numero_orden_label = tk.Label(ventana_agregar_reparacion, text="Número de Orden:")
                    numero_orden_label.pack()
                    numero_orden_entry = tk.Entry(ventana_agregar_reparacion)
                    numero_orden_entry.pack()

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
                    boton_agregar.pack()

                boton_agregar_reparacion = tk.Button(ventana_personalizado, text="Agregar a Reparación", command=agregar_a_reparacion)
                boton_agregar_reparacion.pack()

            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor numérico válido")

        boton_calcular_personalizado = tk.Button(ventana_personalizado, text="Calcular", command=calcular_personalizado)
        boton_calcular_personalizado.pack()

    boton_calcular_presupuesto = tk.Button(ventana_presupuesto, text="Calcular Presupuesto", command=calcular_presupuesto)
    boton_calcular_presupuesto.pack()

    boton_presupuesto_personalizado = tk.Button(ventana_presupuesto, text="Agregar Presupuesto Personalizado", command=agregar_presupuesto_personalizado)
    boton_presupuesto_personalizado.pack()