from tkinter import *
root = Tk()

marco_principal = Frame()
marco_principal2 = Frame()
marco_principal3 = Frame()
marco_principal4 = Frame()
marco_principal5 = Frame()
marco_principal6 = Frame()

marco_principal.grid(row=0, column=0)
marco_principal2.grid(row=0, column=1)
marco_principal3.grid(row=1, column=0)
marco_principal4.grid(row=1, column=1)
marco_principal5.grid(row=2, column=0)
marco_principal6.grid(row=2, column=1)


marco_principal.config(width=100, height=100)
marco_principal.config(bg="red")
marco_principal2.config(width=100, height=100)
marco_principal2.config(bg="gray")
marco_principal3.config(width=100, height=100)
marco_principal3.config(bg="blue")
marco_principal4.config(width=100, height=100)
marco_principal4.config(bg="yellow")
marco_principal5.config(width=100, height=100)
marco_principal5.config(bg="green")
marco_principal6.config(width=100, height=100)
marco_principal6.config(bg="orange")

boton = Button(root, text="click", bg="red", padx=100, pady=25, state=DISABLED).grid(row=1, column=2)

root.mainloop()