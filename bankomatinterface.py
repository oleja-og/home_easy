from tkinter import *
import json

class Login(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.entry1 = Entry(self,font=('Arial', 14))
        self.entry2 = Entry(self,show="*",font=('Arial', 14))
        self.button = Button(text='enter pin', width=15, height=2, command=self.choice)
        self.entry1.place(x=900, y=500)
        self.entry2.place(x=900, y=550)
        self.button.place(x=930, y=600)

    def choice(self):
        name = self.entry1.get()
        password = self.entry2.get()
        with open("users.json", "r") as read_file:
            data = json.load(read_file)
        if name in data and name != "admin":
            if password == data[name]:
                self.destroy()
                Choice().mainloop()
        if name == "admin":
            if password == data[name]:
                self.destroy()
                Admin().mainloop()


class Admin(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.entry1 = Entry(self, show=None, font=('Arial', 14))
        self.entry2 = Entry(self, show='*', font=('Arial', 14))
        self.button = Button(self, text='enter pin', width=15, height=2, command=None)
        self.label = Label(self, text='MAKE YOUR CHOICE', font=('Arial', 30))
        self.label.place(x=900, y=500)
        self.entry1.place(x=900, y=500)
        self.entry2.place(x=900, y=550)
        self.button.place(x=930, y=600)


class Choice(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.button1 = Button(self, text='USD',bg="red", width=15, height=2, command=self.usd)
        self.button2 = Button(self, text='BYN',bg="blue", width=15, height=2, command=self.byn)
        self.button3 = Button(self, text='BALANCE', width=15, height=2, command=self.balance)
        self.label = Label(self, text='MAKE YOUR CHOICE', font=('Arial', 30))
        self.label.place(x=900, y=500)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=1500, y=600)
        self.button3.place(x=1500, y=700)

    def balance(self):
        self.destroy()
        Balance().mainloop()

    def usd(self):
        self.destroy()
        Usd().mainloop()

    def byn(self):
        self.destroy()
        Byn().mainloop()


class Balance(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.label = Label(self, text='would you like another operation', font=('Arial', 30))
        self.button1 = Button(self, text='YES', width=15, height=2, command=self.choice)
        self.button2 = Button(self, text='NO', width=15, height=2, command=self.destroy)
        self.label.place(x=700, y=500)
        self.button1.place(x=900, y=550)
        self.button2.place(x=900, y=600)

    def choice(self):
        self.destroy()
        Choice().mainloop()


class Usd(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.button1 = Button(self, text='WITHDRAW MONEY', width=15, height=2, command=self.withdraw_money)
        self.button2 = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=100, y=1000)

    def withdraw_money(self):
        self.destroy()
        Withdrawusd().mainloop()

    def back(self):
        self.destroy()
        Choice().mainloop()


class Byn(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.button1 = Button(self, text='WITHDRAW MONEY', width=15, height=2, command=self.withdraw_money)
        self.button2 = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.label = Label(self, text='enter an amount', font=('Arial', 25))
        self.label.place(x=870, y=450)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=100, y=1000)

    def withdraw_money(self):
        self.destroy()
        Withdrawbyn().mainloop()

    def back(self):
        self.destroy()
        Choice().mainloop()


class Withdrawusd(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.entry1 = Entry(self, show=None, font=('Arial', 14))
        self.label = Label(self, text='enter an amount', font=('Arial', 25))
        self.button1 = Button(self, text='WITHDRAW MONEY', width=15, height=2, command=self.question)
        self.button2 = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.label.place(x=870, y=450)
        self.entry1.place(x=900, y=500)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=100, y=1000)

    def question(self):
        self.destroy()
        Question().mainloop()

    def back(self):
        self.destroy()
        Usd().mainloop()


class Withdrawbyn(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.entry1 = Entry(self, show=None, font=('Arial', 14))
        self.label = Label(self, text='enter an amount', font=('Arial', 25))
        self.button1 = Button(self, text='WITHDRAW MONEY', width=15, height=2, command=self.question)
        self.button2 = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.label.place(x=870, y=450)
        self.entry1.place(x=900, y=500)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=100, y=1000)

    def question(self):
        self.destroy()
        Question().mainloop()

    def back(self):
        self.destroy()
        Byn().mainloop()


class Question(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.label = Label(self, text='would you like another operation', font=('Arial', 30))
        self.button1 = Button(self, text='YES', width=15, height=2, command=self.choice)
        self.button2 = Button(self, text='NO', width=15, height=2, command=self.destroy)
        self.label.place(x=700, y=500)
        self.button1.place(x=900, y=550)
        self.button2.place(x=900, y=600)

    def choice(self):
        self.destroy()
        Choice().mainloop()


if __name__ == '__main__':
    Login().mainloop()
