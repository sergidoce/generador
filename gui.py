from tkinter import *
from generador import Generador


HEIGHT = 700
WIDTH = 1200

dies = ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres']
hores = ['8-9h', '9-10h', '10-11h', '11-12h', '12-13h', '13-14h', '14-15h', '15-16h', '16-17h', '17-18h', '18-19h', '19-20h', '20-21h']


root = Tk()
root.resizable(0, 0)
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = Frame(root, bg = '#80c1ff')
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

horari_frame = Frame(root, bg = 'green')
horari_frame.place(relx = 0.3, rely = 0, relwidth = 0.7, relheight = 1)

    
frame_assig = Frame(frame, bg = 'red')
frame_assig.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)

label = Label(frame_assig, text = "Escolliu les assignatures que voleu cursar", padx = 35, pady = 20)
label.grid(row = 0, column = 0)


list_assig = Listbox(frame_assig)
list_assig.place(relx = 0.2, relwidth = 0.2)

list_selec = Listbox(frame_assig)
list_selec.place(relx = 0.6, relwidth = 0.2)


root.mainloop()


