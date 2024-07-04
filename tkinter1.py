from tkinter import *
root = Tk()

titulo1 = Label(root, text="Noroeste").pack(anchor=NW)
titulo1 = Label(root, text="Norte").pack(anchor=N)
titulo1 = Label(root, text="Este").pack(anchor=E)
titulo1 = Label(root, text="Sur").pack(anchor=S)

root.mainloop()