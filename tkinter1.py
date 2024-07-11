from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Titulo de la ventana principal")
root.iconbitmap("img/icon.ico")

def muestra_ventana():
    respuesta = askquestion(title="deberia dejar blablabla?", message="Msg que se muestra")
    if respuesta == "no":
        showinfo(title="a seguir!", message="estupendo")
    if respuesta == "yes":
        respuesta_retry = askretrycancel(title="boton equivocado", message="siga siga")

        if respuesta_retry:
            showinfo(title="a seguir", message="estupendo!")

        else:
            showinfo(title="adios!", message="que tengas un buen dia")

boton1 = Button(root, text="enviar",
                command=muestra_ventana,
                width=75).pack()

root.mainloop()