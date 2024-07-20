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
      text="registro para nuevos clientes",
      font="calibri 18",
      fg="red").grid(row=0, columnspan=2)

Label(root,
		text="Nombre").grid(row=1, column=0, pady=10)

e_nombre = Entry(root)
e_nombre.grid(row=1, column=1, pady=10)

Label(root,
		text="Apellidos").grid(row=2, column=0, pady=10)

e_apellidos = Entry(root)
e_apellidos.grid(row=2, column=1, pady=10)

Label(root,
		text="Teléfono").grid(row=3, column=0, pady=10)

e_telefono = Entry(root)
e_telefono.grid(row=3, column=1, pady=10)

Label(root,
		text="Dirección").grid(row=4, column=0, pady=10)

e_direccion = Entry(root)
e_direccion.grid(row=4, column=1, pady=10)

# logica
def registro_cliente():
	nombre = e_nombre.get()
	apellidos = e_apellidos.get()
	telefono = e_telefono.get()
	direccion = e_direccion.get()

	try:
		cursor.execute("INSERT INTO clientes (nombre, apellidos, telefono, direccion) VALUES (?, ?, ?, ?)",
		(nombre, apellidos, telefono, direccion))
		conexion.commit()

	except mariadb.Error as error_registro:
		print(f"Error en el registro: {error_registro}")

boton = Button(root, text="Registrar", width=20, command=registro_cliente).grid(row=5, columnspan=2)

root.mainloop()