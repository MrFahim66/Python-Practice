import tkinter as tk
from tkinter import font as tkfont
import time

current_balance = 50000


class ATM_APP_BETA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Algerian', size=18, weight="bold", slant="italic")

        self.shared_data = {'Balance': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositePage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    # color code: #1D2D50

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#1D2D50')
        self.controller = controller
        self.controller.title("SECURO SERVEX")
        self.controller.state('zoomed')
        self.controller.iconphoto(True, tk.PhotoImage(file='atm.png'))

        headingLabel1 = tk.Label(self,
                                 text="SECURO SERVEX ATM",
                                 font=('Algerian', 70, 'bold'),
                                 fg='white',
                                 bg='#1D2D50')
        headingLabel1.pack(pady=25)

        space_Label = tk.Label(self, text="USER : FAHIM UR RAHMAN",
                               font=('Algerian', 30, 'bold'), height=2,
                               fg='white', bg="#1D2D50")
        space_Label.pack()

        pass_Label = tk.Label(self, text="Enter Your Password",
                              font=('Algerian', 30, 'bold'), bg="#1D2D50", fg='white')
        pass_Label.pack(pady=25)

        user_password = tk.StringVar()
        pass_entry_box = tk.Entry(self,
                                  textvariable=user_password,
                                  font=('Algerian', 20), width=30)
        pass_entry_box.focus_set()
        pass_entry_box.pack(ipady=10)

        def handle_focus_in():
            pass_entry_box.configure(fg='black', show="#")

        pass_entry_box.bind("<FocusIn>", handle_focus_in())

        def check_password():
            if user_password.get() == 'eagnas':
                user_password.set('')
                incorrect_pass_label['text'] = ""
                controller.show_frame('MenuPage')
            else:
                incorrect_pass_label['text'] = "Incorrect Password"

        enter_button = tk.Button(self,
                                 text="Enter",
                                 font=('ALgerian', 25, 'bold'),
                                 command=check_password,
                                 relief="groove",
                                 borderwidth=4,
                                 width=20,
                                 height=2,
                                 bg='#1E5F74',
                                 fg='white')
        enter_button.pack(pady=25)

        incorrect_pass_label = tk.Label(self,
                                        text="",
                                        font=('Algerian', 40, 'bold', 'underline'),
                                        fg='red',
                                        bg='#133B5C'
                                        )
        incorrect_pass_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief="solid", borderwidth=3, bg="#1D2D50")
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo, bg="#1D2D50")
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file='credit-card.png')
        master_label = tk.Label(bottom_frame, image=master_card_photo, bg="#1D2D50")
        master_label.pack(side='left')
        master_label.image = master_card_photo

        def time_show():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, time_show)

        time_label = tk.Label(bottom_frame, font=('Algerian', 20), bg="#1D2D50", fg='white')
        time_label.pack(side='right')

        time_show()


class MenuPage(tk.Frame):
    # color code : #1D2D50

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1D2D50")
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="SECURO SERVEX ATM",
                                 font=('Algerian', 70, 'bold'),
                                 fg='white',
                                 bg='#1D2D50')
        headingLabel1.pack(pady=15)

        space_Label = tk.Label(self,
                               text="USER : FAHIM UR RAHMAN",
                               font=('Algerian', 30, 'bold'),
                               height=2,
                               fg='white', bg="#1D2D50")
        space_Label.pack()

        main_menu_label = tk.Label(self,
                                   text="Main Menu",
                                   font=('Algerian', 50),
                                   fg='white',
                                   bg="#1D2D50")
        main_menu_label.pack(pady=15)

        selection_label = tk.Label(self,
                                   text="Make Your Selection:",
                                   font=("Algerian", 20),
                                   fg='white',
                                   bg="#133B5C",
                                   )
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg="#1E5F74")
        button_frame.pack(fill='both', expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')

        wintdraw_button = tk.Button(button_frame,
                                    text="Withdraw",
                                    font=('Algerian', 15, 'bold'),
                                    command=withdraw,
                                    relief='solid',
                                    borderwidth=3,
                                    width=50,
                                    height=5,
                                    anchor='center')
        wintdraw_button.pack(pady=5)

        def deposit():
            controller.show_frame('DepositePage')

        deposit_button = tk.Button(button_frame,
                                   text="Deposit",
                                   font=('Algerian', 15, 'bold'),
                                   command=deposit,
                                   relief='solid',
                                   borderwidth=3,
                                   width=50,
                                   height=5,
                                   anchor='center')
        deposit_button.pack(pady=5)

        def balance():
            controller.show_frame('BalancePage')

        balance_button = tk.Button(button_frame,
                                   text="Balance",
                                   font=('Algerian', 15, 'bold'),
                                   command=balance,
                                   relief='solid',
                                   borderwidth=3,
                                   width=50,
                                   height=5,
                                   anchor='center')
        balance_button.pack(pady=5)

        def exit():
            controller.show_frame('StartPage')

        exit_button = tk.Button(button_frame,
                                text="Exit To Main Menu",
                                font=('Algerian', 15, 'bold'),
                                command=exit,
                                relief='solid',
                                borderwidth=3,
                                width=50,
                                height=5,
                                anchor='center')
        exit_button.pack(pady=5)

        bottom_frame = tk.Frame(self, relief="solid", borderwidth=3, bg="#1D2D50")
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo, bg="#1D2D50")
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file='credit-card.png')
        master_label = tk.Label(bottom_frame, image=master_card_photo, bg="#1D2D50")
        master_label.pack(side='left')
        master_label.image = master_card_photo

        def time_show():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, time_show)

        time_label = tk.Label(bottom_frame, font=('Algerian', 20), bg="#1D2D50", fg='white')
        time_label.pack(side='right')

        time_show()


class WithdrawPage(tk.Frame):
    # color code : #1D2D50

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1D2D50")
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="SECURO SERVEX ATM",
                                 font=('Algerian', 70, 'bold'),
                                 fg='white',
                                 bg='#1D2D50')
        headingLabel1.pack(pady=20)

        space_Label = tk.Label(self,
                               text="USER : FAHIM UR RAHMAN",
                               font=('Algerian', 20, 'bold'),
                               height=2,
                               fg='white', bg="#1D2D50")
        space_Label.pack()

        choose_amount_label = tk.Label(self,
                                       text="Choose The Amount That You Want To Withdraw",
                                       font=('Algerian', 30),
                                       fg='white',
                                       bg="#1D2D50")
        choose_amount_label.pack(pady=10)

        button_frame = tk.Frame(self, bg="#1E5F74")
        button_frame.pack(fill='both', expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')

        twenty_button = tk.Button(button_frame,
                                  text='20',
                                  command=lambda: withdraw(20),
                                  font=('Arial', 15, 'bold'),
                                  relief="solid",
                                  borderwidth=3,
                                  width=40,
                                  height=2,
                                  anchor='center')
        twenty_button.pack(pady=15)

        fifty_button = tk.Button(button_frame,
                                 text='50',
                                 command=lambda: withdraw(50),
                                 font=('Arial', 15, 'bold'),
                                 relief="solid",
                                 borderwidth=3,
                                 width=40,
                                 height=2,
                                 anchor='center')
        fifty_button.pack(pady=15)

        hundred_button = tk.Button(button_frame,
                                   text='100',
                                   command=lambda: withdraw(100),
                                   font=('Arial', 15, 'bold'),
                                   relief="solid",
                                   borderwidth=3,
                                   width=40,
                                   height=2,
                                   anchor='center')
        hundred_button.pack(pady=15)

        five_hundred_button = tk.Button(button_frame,
                                        text='500',
                                        command=lambda: withdraw(500),
                                        font=('Arial', 15, 'bold'),
                                        relief="solid",
                                        borderwidth=3,
                                        width=40,
                                        height=2,
                                        anchor='center')
        five_hundred_button.pack(pady=15)

        thousand_button = tk.Button(button_frame,
                                    text='1000',
                                    command=lambda: withdraw(1000),
                                    font=('Arial', 15, 'bold'),
                                    relief="solid",
                                    borderwidth=3,
                                    width=40,
                                    height=2,
                                    anchor='center')
        thousand_button.pack(pady=15)

        cash = tk.StringVar()

        other_amount_entry = tk.Entry(button_frame,
                                      textvariable=cash,
                                      font=('Arial', 15, 'bold'),
                                      relief="solid",
                                      borderwidth=3,
                                      width=50,
                                      justify='left')
        other_amount_entry.pack(pady=15, ipady=60)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')

        other_amount_entry.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief="solid", borderwidth=3, bg="#1D2D50")
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo, bg="#1D2D50")
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file='credit-card.png')
        master_label = tk.Label(bottom_frame, image=master_card_photo, bg="#1D2D50")
        master_label.pack(side='left')
        master_label.image = master_card_photo

        def time_show():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, time_show)

        time_label = tk.Label(bottom_frame, font=('Algerian', 20), bg="#1D2D50", fg='white')
        time_label.pack(side='right')

        time_show()


class DepositePage(tk.Frame):
    # color code : #1D2D50

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1D2D50")
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="SECURO SERVEX ATM",
                                 font=('Algerian', 70, 'bold'),
                                 fg='white',
                                 bg='#1D2D50')
        headingLabel1.pack(pady=20)

        space_Label = tk.Label(self,
                               text="USER : FAHIM UR RAHMAN",
                               font=('Algerian', 30, 'bold'), height=2,
                               fg='white', bg="#1D2D50")
        space_Label.pack()

        deposit_Label = tk.Label(self,
                                 text="Enter Amount To Deposit",
                                 font=('Algerian', 30, 'bold'), bg="#1D2D50", fg='white')
        deposit_Label.pack(pady=20)

        cash = tk.StringVar()

        deposit_amount_entry = tk.Entry(self,
                                        textvariable=cash,
                                        font=('Arial', 25, 'bold'),
                                        relief="solid",
                                        borderwidth=3,
                                        width=50,
                                        justify='left')
        deposit_amount_entry.pack(pady=15, ipady=60)

        def deposite_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')

        enter_button = tk.Button(self,
                                 text="ENTER",
                                 font=('Algerian', 15, 'bold'),
                                 command=deposite_cash,
                                 relief='solid',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        enter_button.pack(pady=20)

        two_tone_label = tk.Label(self, bg="#334257")
        two_tone_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief="solid", borderwidth=3, bg="#1D2D50")
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo, bg="#1D2D50")
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file='credit-card.png')
        master_label = tk.Label(bottom_frame, image=master_card_photo, bg="#1D2D50")
        master_label.pack(side='left')
        master_label.image = master_card_photo

        def time_show():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, time_show)

        time_label = tk.Label(bottom_frame, font=('Algerian', 20), bg="#1D2D50", fg='white')
        time_label.pack(side='right')

        time_show()


class BalancePage(tk.Frame):
    # color code : #1D2D50

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1D2D50")
        self.controller = controller

        headingLabel1 = tk.Label(self,
                                 text="SECURO SERVEX ATM",
                                 font=('Algerian', 70, 'bold'),
                                 fg='white',
                                 bg='#1D2D50')
        headingLabel1.pack(pady=25)

        space_Label = tk.Label(self,
                               text="USER : FAHIM UR RAHMAN",
                               font=('Algerian', 30, 'bold'), height=2,
                               fg='white', bg="#1D2D50")
        space_Label.pack()

        headingLabel_balance = tk.Label(self,
                                        text="Your current account balance is",
                                        font=('Algerian', 40, 'bold'),
                                        fg='white',
                                        bg='#1D2D50')
        headingLabel_balance.pack(pady=25)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)

        balance_Label = tk.Label(self,
                                 textvariable=controller.shared_data['Balance'],
                                 font=('Algerian', 40, 'bold'), bg="#133B5C", fg='white')
        balance_Label.pack(pady=25)

        button_frame = tk.Frame(self, bg="#1E5F74")
        button_frame.pack(fill='both', expand=True)

        def exit():
            controller.show_frame('MenuPage')

        exit_button = tk.Button(button_frame, text="Exit",
                                font=('Algerian', 15, 'bold'),
                                command=exit,
                                relief='solid',
                                borderwidth=3,
                                width=50,
                                height=5,
                                anchor='center')
        exit_button.pack(pady=25)

        def exit_Menu():
            controller.show_frame('StartPage')

        exit_button = tk.Button(button_frame, text="Exit To Main Menu",
                                font=('Algerian', 15, 'bold'),
                                command=exit_Menu,
                                relief='solid',
                                borderwidth=3,
                                width=50,
                                height=5,
                                anchor='center')
        exit_button.pack(pady=25)

        bottom_frame = tk.Frame(self, relief="solid", borderwidth=3, bg="#1D2D50")
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo, bg="#1D2D50")
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file='credit-card.png')
        master_label = tk.Label(bottom_frame, image=master_card_photo, bg="#1D2D50")
        master_label.pack(side='left')
        master_label.image = master_card_photo

        def time_show():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, time_show)

        time_label = tk.Label(bottom_frame, font=('Algerian', 20), bg="#1D2D50", fg='white')
        time_label.pack(side='right')

        time_show()


if __name__ == "__main__":
    app = ATM_APP_BETA()
    app.mainloop()
