from tkinter import *
root = Tk()

rbtn = IntVar()
rbtn.set(value=1)

def actualiza(value):
    opcion_set = Label(root, text=value).grid(row=3)


titulo = Label(root, text="seleccione").grid(row=0)

opcion_1 = Radiobutton(root, text="primera opcion", value=1, variable=rbtn,
                       command=lambda : actualiza(rbtn.get())).grid(row=1)
opcion_2 = Radiobutton(root, text="segunda opcion", value=2, variable=rbtn,
                       command=lambda : actualiza(rbtn.get())).grid(row=2)

root.mainloop()