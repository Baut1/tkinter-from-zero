from tkinter import *
root = Tk()

texto = Label(root, text="introduzca sus datos").grid(row=0, column=0)

user = Entry(root, width=50)
user.grid(row=1, column=0)

password = Entry(root, width=50, show="*")
password.grid(row=2, column=0)

def click_boton():
    texto = Label(root, text=f'"{user.get()}" inicio sesion').grid(row=0, column=0)

boton = Button(root, text="enviar", bg="red", padx=100, pady=25,
               command=click_boton).grid(row=3, column=0)

root.mainloop()