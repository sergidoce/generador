from tkinter import *

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
for x in range(6):
    Grid.columnconfigure(horari_frame, x, weight=1)
 
for x in range(len(hores)+1):
    Grid.rowconfigure(horari_frame, x, weight=1)

for i in range (0, 5):
    label = Label(horari_frame, width = 20, height = 4, text = dies[i], justify = CENTER, padx = 1, pady = 1)
    label.grid(row = 0, column = i+1, padx = 1, pady = 4)

for i in range (0, len(hores)):
    label = Label(horari_frame, width = 15, height = 4, text = hores[i], justify = CENTER, padx = 1, pady = 1)
    label.grid(row = i+1, column = 0, padx = 1, pady = 1)

root.mainloop()