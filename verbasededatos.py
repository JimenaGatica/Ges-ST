import sqlite3

def mostrar_usuarios():
    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()

        if not resultados:
            print("No hay usuarios registrados.")
        else:
            print("Lista de Usuarios:")
            for fila in resultados:
                print(f"Nombre: {fila[0]}, Usuario: {fila[1]}, Contraseña: {fila[2]}")

        conexion.close()

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")

if __name__ == "__main__":
    mostrar_usuarios()