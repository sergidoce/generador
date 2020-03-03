import tkinter as tk

HEIGHT = 700
WIDTH = 1200

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff')
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

horari_frame = tk.Frame(root, bg = 'green')
horari_frame.place(relx = 0.3, rely = 0, relwidth = 0.7, relheight = 1)

root.mainloop()