from tkinter import *
root = Tk()

def click_boton():
    texto = Label(root, text="dont click again").grid(row=0, column=1)

boton = Button(root, text="dont click", bg="red", padx=100, pady=25,
               command=click_boton).grid(row=0, column=0)

root.mainloop()