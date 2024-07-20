from tkinter import *
import mariadb

root = Tk()
root.title("ventana principal")
root.geometry('300x200')

# conexion
try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="tkinterdesdecero"
    )
    # Label(root, text="Se conecto correctamente a la base de datos: " + conexion.database).pack()
    cursor = conexion.cursor()

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos {error}")
    exit(1)

# interfaz grafica
Label(root,
      text="eliminar tabla o base de datos",
      font="calibri 18",
      fg="red").grid(row=0, columnspan=2)

Label(root,
		text="Tabla").grid(row=1, column=0, pady=10)

e_tabla = Entry(root)
e_tabla.grid(row=1, column=1, pady=10)

Label(root,
		text="Base de datos").grid(row=2, column=0, pady=10)

e_base_datos = Entry(root)
e_base_datos.grid(row=2, column=1, pady=10)

# logica
def eliminar_tabla():
    tabla = e_tabla.get()
    try:
        cursor.execute(f"DROP TABLE {tabla}")
        cursor.commit()
    except mariadb.Error as error_tabla:
        print(f"Error al eliminar la tabla: {error_tabla}")

def eliminar_base_datos():
    base_datos = e_base_datos.get()
    try:
        cursor.execute(f"DROP DATABASE {base_datos}")
        cursor.commit()
    except mariadb.Error as error_base_datos:
        print(f"Error al eliminar la base de datos: {error_base_datos}")

boton1 = Button(root, text="elim tabla", width=20, command=eliminar_tabla).grid(row=5, column=0)
boton2 = Button(root, text="elim bdd", width=20, command=eliminar_base_datos).grid(row=5, column=1)

root.mainloop()