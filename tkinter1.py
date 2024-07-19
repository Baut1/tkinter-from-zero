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

except mariadb.Error as error:
    print(f"Error al conectar con la base de datos {error}")
    exit(1)

root.mainloop()