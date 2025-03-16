import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

def crear_usuario(actualizar_tabla):
    ventana_crear_usuario = tk.Toplevel()
    ventana_crear_usuario.title("Crear Nuevo Usuario - Sistema de Gestión")
    ventana_crear_usuario.geometry("1200x900+50+50")
    ventana_crear_usuario.configure(bg="snow2")

    nombre_label = tk.Label(ventana_crear_usuario, text="Nombre:", font=("Arial", 12), bg="#E0F2F7")
    nombre_label.place(relx=0.2, rely=0.15, anchor=tk.W)
    nombre_entry = tk.Entry(ventana_crear_usuario, font=("Arial", 12))
    nombre_entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    usuario_label = tk.Label(ventana_crear_usuario, text="Usuario:", font=("Arial", 12), bg="#E0F2F7")
    usuario_label.place(relx=0.2, rely=0.3, anchor=tk.W)
    usuario_entry = tk.Entry(ventana_crear_usuario, font=("Arial", 12))
    usuario_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    clave_label = tk.Label(ventana_crear_usuario, text="Contraseña:", font=("Arial", 12), bg="#E0F2F7")
    clave_label.place(relx=0.2, rely=0.45, anchor=tk.W)
    clave_entry = tk.Entry(ventana_crear_usuario, show="*", font=("Arial", 12))
    clave_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    rol_label = tk.Label(ventana_crear_usuario, text="Rol:", font=("Arial", 12), bg="#E0F2F7")
    rol_label.place(relx=0.2, rely=0.6, anchor=tk.W)
    roles = ["Administrador", "Técnico", "Atención al Público"]
    rol_combobox = tk.StringVar(ventana_crear_usuario)
    rol_combobox.set(roles[0])
    rol_menu = tk.OptionMenu(ventana_crear_usuario, rol_combobox, *roles)
    rol_menu.config(font=("Arial", 12))
    rol_menu.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def guardar_usuario():
        nombre = nombre_entry.get()
        usuario = usuario_entry.get()
        clave = clave_entry.get()
        rol = rol_combobox.get()
        fecha_creacion = datetime.now().strftime("%d-%m-%Y %H:%M")

        if not nombre or not usuario or not clave or not rol:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, usuario TEXT, clave TEXT, rol TEXT, fecha_creacion TEXT, fecha_baja TEXT)")
            cursor.execute("INSERT INTO usuarios (nombre, usuario, clave, rol, fecha_creacion) VALUES (?, ?, ?, ?, ?)", (nombre, usuario, clave, rol, fecha_creacion))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario creado correctamente")
            ventana_crear_usuario.destroy()
            actualizar_tabla() # Llama a la función para actualizar la tabla
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al crear el usuario: {e}")

    boton_guardar = tk.Button(ventana_crear_usuario, text="Guardar", command=guardar_usuario, font=("Arial", 12), bg="#B2EBF2", padx=20, pady=10)
    boton_guardar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def gestion_usuarios():
    ventana_gestion = tk.Toplevel()
    ventana_gestion.title("Gestión de Usuarios")
    ventana_gestion.geometry("1100x600+50+0")
    ventana_gestion.configure(bg="snow2")

    def eliminar_usuario():
        ventana_eliminar = tk.Toplevel(ventana_gestion)
        ventana_eliminar.title("Eliminar Usuario")
        ventana_eliminar.geometry("400x200+350+250")
        ventana_eliminar.configure(bg="snow2")

        try:
            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM usuarios")
            usuarios_lista = [row[0] for row in cursor.fetchall()]
            conexion.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar la lista de usuarios: {e}")
            return

        usuario_seleccionado = tk.StringVar(ventana_eliminar)
        usuario_seleccionado.set("Seleccionar usuario")

        lista_usuarios_menu = tk.OptionMenu(ventana_eliminar, usuario_seleccionado, *usuarios_lista)
        lista_usuarios_menu.config(font=("Arial", 12))
        lista_usuarios_menu.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        def confirmar_eliminar():
            usuario_a_eliminar = usuario_seleccionado.get()
            if usuario_a_eliminar == "Seleccionar usuario":
                messagebox.showerror("Error", "Por favor, selecciona un usuario para eliminar.")
                return

            fecha_baja = datetime.now().strftime("%d-%m-%Y %H:%M")
            try:
                conexion = sqlite3.connect("usuarios.db")
                cursor = conexion.cursor()
                cursor.execute("UPDATE usuarios SET fecha_baja = ? WHERE usuario = ?", (fecha_baja, usuario_a_eliminar))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", f"Usuario '{usuario_a_eliminar}' eliminado correctamente.")
                ventana_eliminar.destroy()
                mostrar_usuarios() # Actualizar la lista después de eliminar
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al eliminar el usuario: {e}")

        boton_eliminar_confirmar = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminar, font=("Arial", 12), bg="#F44336", fg="white", padx=20, pady=10)
        boton_eliminar_confirmar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def mostrar_usuarios():
        # Limpiar la tabla si ya existe
        for item in tabla_usuarios.get_children():
            tabla_usuarios.delete(item)

        try:
            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, usuario, rol, fecha_creacion, fecha_baja FROM usuarios")
            usuarios_data = cursor.fetchall()
            conexion.close()

            for usuario in usuarios_data:
                fecha_baja_str = usuario[4] if usuario[4] else "Activo"
                tabla_usuarios.insert("", tk.END, values=(usuario[0], usuario[1], usuario[2], usuario[3], fecha_baja_str))

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar la lista de usuarios: {e}")

    boton_crear = tk.Button(ventana_gestion, text="Crear Nuevo Usuario", command=lambda: crear_usuario(mostrar_usuarios), font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10)
    boton_crear.place(relx=0.2, rely=0.1, anchor=tk.W)

    boton_eliminar = tk.Button(ventana_gestion, text="Eliminar Usuario", command=eliminar_usuario, font=("Arial", 12), bg="#F44336", fg="white", padx=20, pady=10)
    boton_eliminar.place(relx=0.7, rely=0.1, anchor=tk.W)

    boton_salir_gestion = tk.Button(ventana_gestion, text="Salir", command=ventana_gestion.destroy, font=("Arial", 12), bg="#FFC107", padx=20, pady=10)
    boton_salir_gestion.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    # Crear la tabla Treeview
    tabla_usuarios = ttk.Treeview(ventana_gestion, columns=("Nombre", "Usuario", "Rol", "Fecha Alta", "Fecha Baja"), show="headings")
    tabla_usuarios.heading("Nombre", text="Nombre")
    tabla_usuarios.heading("Usuario", text="Usuario")
    tabla_usuarios.heading("Rol", text="Rol")
    tabla_usuarios.heading("Fecha Alta", text="Fecha Alta")
    tabla_usuarios.heading("Fecha Baja", text="Fecha Baja")

    # Ajustar el ancho de las columnas
    tabla_usuarios.column("Nombre", width=150)
    tabla_usuarios.column("Usuario", width=150)
    tabla_usuarios.column("Rol", width=100)
    tabla_usuarios.column("Fecha Alta", width=180)
    tabla_usuarios.column("Fecha Baja", width=180)

    tabla_usuarios.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=900, height=400)

    mostrar_usuarios() # Mostrar la lista de usuarios al abrir la ventana de gestión

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    gestion_usuarios()
    root.mainloop()