from tkinter import *
from generador import Generador
from dades import Dades

def on_select(event):
    print(event.widget.curselection())


HEIGHT = 700
WIDTH = 900

root = Tk()
root.resizable(0, 0)
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

llista = Listbox(root)
llista.place(relwidth = 0.1, relheight = 0.3)
llista.bind('<<ListboxSelect>>', on_select)
llista.insert(END, "test")
llista.insert(END, "test2")




root.mainloop()