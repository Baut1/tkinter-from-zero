from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Titulo de la ventana principal")
root.iconbitmap("img/icon.ico")

def muestra_ventana():
    askretrycancel(title="deberia dejar blablabla?", message="Msg que se muestra")

boton1 = Button(root, text="enviar",
                command=muestra_ventana,
                width=75).pack()

root.mainloop()