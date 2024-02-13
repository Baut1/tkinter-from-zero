from tkinter import *
root = Tk()

def actualiza(value):
    opcion_set = Label(root, text=value).pack()

titulo = Label(root, text="seleccione").pack()

opciones = [["Color rojo", "rojo"],
            ["Color azul", "azul"],
            ["Color verde", "verde"],
            ["Color amarillo", "amarillo"]]

colores = StringVar()
colores.set("rojo")

for opcion, valor in opciones:
    Radiobutton(root, text=opcion, value=valor, variable=colores).pack()

boton_envia = Button(root, text="send", command=lambda : actualiza(colores.get())).pack()

root.mainloop()