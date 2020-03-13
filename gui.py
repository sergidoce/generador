from tkinter import *
from generador import Generador
from dades import Dades

def is_in_list(elemento):
    for i in range(0, list_selec.size()):
        x = list_selec.get(i)
        
        if x == elemento:
            return True
    return False

def on_select_1(event):
    selec = event.widget.curselection()
    elemento = list_assig.get(selec[0])

    if not is_in_list(elemento):
        list_selec.insert(END, list_assig.get(selec[0]))


def on_select_2(event):
    selec2 = event.widget.curselection()
    list_selec.delete(selec2[0])


def posar_assigs():
    for assignatura in assignatures:
        list_assig.insert(END, assignatura)


def update_list():
    search_term = search_var.get()

    list_assig.delete(0, END)

    for item in assignatures:
        if search_term.lower() in item.lower():
            list_assig.insert(END, item)

HEIGHT = 700
WIDTH = 1200

dies = ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres']
hores = ['8-9h', '9-10h', '10-11h', '11-12h', '12-13h', '13-14h', '14-15h', '15-16h', '16-17h', '17-18h', '18-19h', '19-20h', '20-21h']

#Creació de tots els frames

root = Tk()
root.resizable(0, 0)
canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = Frame(root, bg = '#80c1ff')
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

frame_top_left = Frame(frame, bg = 'yellow')
frame_top_left.place(relwidth = 1, relheight = 0.1)

frame_assig = Frame(frame, bg = 'red')
frame_assig.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.5)

horari_frame = Frame(root, bg = 'green')
horari_frame.place(relx = 0.3, rely = 0, relwidth = 0.7, relheight = 1)



#Creació de widgets

label = Label(frame_top_left, text = "Escolliu les assignatures que voleu cursar", bg = 'yellow', font = ("Consolas, 12"))
label.place( relx = 0.1, rely = 0.2, anchor = 'nw')

search_var = StringVar()
search_var.trace("w", lambda name, index, mode: update_list())

search = Entry(frame_top_left, textvariable = search_var, bg='purple')
search.place(relx = 0.1, rely = 0.8, anchor = 'w', relwidth = 0.3)

list_assig = Listbox(frame_assig)
list_assig.place(relx = 0.1, relwidth = 0.3)
list_assig.bind('<<ListboxSelect>>', on_select_1)

list_selec = Listbox(frame_assig)
list_selec.place(relx = 0.6, relwidth = 0.3)
list_selec.bind('<<ListboxSelect>>', on_select_2)

dades = Dades()
assignatures = dades.get_assignatures()

posar_assigs()



root.mainloop()


