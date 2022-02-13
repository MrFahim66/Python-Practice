import tkinter as tk

HEIGHT = 800
WIDTH = 1000

def printMsge(entry):
    tk.Label(lower_frame, text = entry).pack()

root = tk.Tk()
root.title("Python GUI Project")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = tk.Frame(root, bg='#1a6edb')
frame1.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#35c4e8', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg='light green', font=60, bd=5)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, font=60, text="See Your Entry Here:", bg='#63ebc6', fg='blue', activebackground='#12dbca', bd=5, command = lambda : printMsge(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#35c4e8', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=1, anchor='n')

label = tk.Label(lower_frame, text="This is The Label", bg='light blue', font = 60)
label.place(relwidth=1, relheight=1)

root.mainloop()
