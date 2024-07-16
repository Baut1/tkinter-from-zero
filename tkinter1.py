from tkinter import *

root = Tk()
root.title("ventana principal")
root.geometry('300x200')

def envia_boton():
    ventana_nueva = Toplevel()
    ventana_nueva.title("ventana secundaria")
    ventana_nueva.geometry("300x200")
    valor_entrada = entrada.get()
    etiqueta = Label(ventana_nueva, text=valor_entrada).grid(row=0)
    cerrar_ventana = Button(root, text="cerrar nueva ventana", command=ventana_nueva.destroy).grid(row=2)

entrada = Entry(root, width=20)
entrada.grid(row=0)

envia = Button(root, command=envia_boton, text="enviar").grid(row=1)
cerrar_root = Button(root, command=root.destroy, text="cerrar ventana principal").grid(row=3)

root.mainloop()