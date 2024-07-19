from tkinter import *
import mariadb

root = Tk()
root.title("ventana principal")
root.geometry('300x200')

try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="tkinterdesdecero"
    )
    Label(root, text="Se conecto correctamente a la base de datos: " + conexion.database).pack()
    cursor = conexion.cursor()

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos {error}")
    exit(1)

def crear_tabla():
    try:
        cursor.execute("CREATE TABLE clientes (id INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(32) NOT NULL, apellidos VARCHAR(64) NOT NULL, telefono VARCHAR (9) NOT NULL, direccion VARCHAR(256), PRIMARY KEY (id))")
        conexion.commit()
    except mariadb.Error as error_tabla:
        print(f"error al crear la tabla: {error_tabla}")

boton = Button(root, text="crear tabla", width=20, command=crear_tabla)
boton.place(x=25, y=10)

root.mainloop()