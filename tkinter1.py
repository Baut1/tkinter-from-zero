from tkinter import *

root = Tk()
root.title("ventana principal")
root.geometry('300x200')

def seleccion():
    etiqueta1 = Label(root, text=control1.get()).pack()
    etiqueta2 = Label(root, text=control2.get()).pack()

control1 = StringVar()
control2 = StringVar()

opcion_1 = Checkbutton(root, text="opcion 1", variable=control1, onvalue="opcion 1 seleccionada", offvalue="opcion 1 no seleccionada")
opcion_1.pack()
opcion_1.deselect()

opcion_2 = Checkbutton(root, text="opcion 2", variable=control2, onvalue="opcion 2 seleccionada", offvalue="opcion 2 no seleccionada")
opcion_2.pack()
opcion_2.deselect()

muestra_seleccion = Button(root, text="mostrar seleccion", command=seleccion).pack()

root.mainloop()