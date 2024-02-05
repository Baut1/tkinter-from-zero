from tkinter import *
root = Tk()

marco_principal = Frame()
marco_principal.pack()

marco_principal2 = Frame()
marco_principal2.pack()

marco_principal.config(width=400, height=400)
marco_principal.config(bg="red")

marco_principal2.config(width=400, height=400)
marco_principal2.config(bg="blue")

root.mainloop()