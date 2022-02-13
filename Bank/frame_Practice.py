import tkinter as tk

def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.title("Framing Test GUI")
window.state('zoomed')

window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight =1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row =0, column =0, sticky='nsew')

#Frame 1 Code:
frame1_title = tk.Label(frame1, text = "This is Test Frame 1", bg = "#112031", font = ('ALgerian',60, 'bold'), fg ='white')
frame1_title.place(relx = 0, rely = 0 ,relwidth=1, relheight=1)

button = tk.Button(frame1, font=('ALgerian',30, 'bold'), text="Go To Page 2", bg='#63ebc6', fg='blue', activebackground='#12dbca', bd=5, command = lambda : show_frame(frame2))
button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

#Frame 2 Code:
frame2_title = tk.Label(frame2, text = "This is Test Frame 2", bg = "#152D35", font = ('ALgerian',60, 'bold'), fg = 'white')
frame2_title.place(relx = 0, rely = 0 ,relwidth=1, relheight=1)

frame2_button = tk.Button(frame2, font=('ALgerian',30, 'bold'), text="Go To Page 3", bg='#63ebc6', fg='blue', activebackground='#12dbca', bd=5, command = lambda : show_frame(frame3))
frame2_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

#Frame 3 Code:
frame3_title = tk.Label(frame3, text = "This is Test Frame 3", bg = "#345B63", font = ('ALgerian',60, 'bold'), fg = 'white')
frame3_title.place(relx = 0, rely = 0 ,relwidth=1, relheight=1)

frame3_button = tk.Button(frame3, font=('ALgerian',30, 'bold'), text="Go To Page 4", bg='#63ebc6', fg='blue', activebackground='#12dbca', bd=5, command = lambda : show_frame(frame4))
frame3_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

#Frame 4 Code:
frame4_title = tk.Label(frame4, text = "This is Test Frame 4", bg = "#D4ECDD", font = ('ALgerian',60, 'bold'), fg = 'black')
frame4_title.place(relx = 0, rely = 0 ,relwidth=1, relheight=1)

frame4_button = tk.Button(frame4, font = ('ALgerian',30, 'bold'), text="Go To Home Page", bg='#63ebc6', fg='blue', activebackground='#12dbca', bd=5, command = lambda : show_frame(frame1))
frame4_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


show_frame(frame1)

window.mainloop()