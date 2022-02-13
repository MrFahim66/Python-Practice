import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 800
WIDTH = 1000

root = tk.Tk()
root.title("Python GUI Project")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

load = Image.open("D:/Codes/Python/Bank/HMS.jpg")
render = ImageTk.PhotoImage(load)

frame1 = tk.Frame(root, bg='#1a6edb')
frame1.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg = "#98CAEF")
lower_frame.place(relx=0.015, rely=0.025, relwidth=0.97, relheight=0.93)

label2 = tk.Label(lower_frame, text = "HOTEL", font = 180, bg ="#98CAEF" )
label2.place(relwidth = 1, relheight = 1)

label3 = tk.Label(label2, text = "HOTEL")
label3.place()

label = tk.Label(frame1, image = render)
label.image = render
label.place(relwidth=1, relheight=1)


root.mainloop()
