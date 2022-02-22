from tkinter import *
import json

import function
from function import Bankomat, Person


class Login(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.entry1 = Entry(self,font=('Arial', 14))
        self.entry2 = Entry(self,show="*",font=('Arial', 14))
        self.button = Button(text='enter pin', width=15, height=2, command=self.choice)
        self.button1 = Button(text='quit', width=15, height=2, command=self.quit)
        self.entry1.place(x=900, y=500)
        self.entry2.place(x=900, y=550)
        self.button.place(x=930, y=600)
        self.button1.place(x=100, y=1000)

    def quit(self):
        self.destroy()

    def choice(self):
        name = self.entry1.get()
        password = self.entry2.get()
        with open("users.json", "r") as read_file:
            data = json.load(read_file)
            if name in data and name != "admin":
                if password == data[name]:
                    p = Person("oleg", 1111, 2000)
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
        self.button = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.button1 = Button(self, text='recharge USD', width=15, height=2, command=self.recharge_usd)
        self.button2 = Button(self, text='recharge BYN', width=15, height=2, command=self.recharge_byn)
        self.label1 = Label(self, text= "USD", font=('Arial', 30))
        self.label2 = Label(self, text=b.usd, font=('Arial', 30))
        self.label3 = Label(self, text="BYN", font=('Arial', 30))
        self.label4 = Label(self, text=b.byn, font=('Arial', 30))
        self.label1.place(x=100, y=100)
        self.label2.place(x=100, y=200)
        self.label3.place(x=100, y=300)
        self.label4.place(x=100, y=400)
        self.button.place(x=100, y=1000)
        self.button1.place(x=1500, y=100)
        self.button2.place(x=1500, y=300)


    def back(self):
        self.destroy()
        Login().mainloop()

    def recharge_usd(self):
        b.usd = {100: 500, 50: 500, 20: 500, 10: 500, 5: 500}
        self.destroy()
        Admin().mainloop()

    def recharge_byn(self):
        b.byn = {100: 500, 50: 500, 20: 500, 10: 500, 5: 500}
        self.destroy()
        Admin().mainloop()



class Choice(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.button1 = Button(self, text='USD',bg="red", width=15, height=2, command=self.usd)
        self.button2 = Button(self, text='BYN',bg="blue", width=15, height=2, command=self.byn)
        self.button3 = Button(self, text='BALANCE', width=15, height=2, command=self.balance)
        self.button4 = Button(self, text='BACK', width=15, height=2, command=self.back)
        self.label = Label(self, text='MAKE YOUR CHOICE', font=('Arial', 30))
        self.label.place(x=900, y=500)
        self.button1.place(x=1500, y=500)
        self.button2.place(x=1500, y=600)
        self.button3.place(x=1500, y=700)
        self.button4.place(x=100, y=1000)

    def balance(self):
        self.destroy()
        Balance().mainloop()


    def usd(self):
        self.destroy()
        Usd().mainloop()

    def byn(self):
        self.destroy()
        Byn().mainloop()

    def back(self):
        self.destroy()
        Login().mainloop()


class Balance(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.attributes("-fullscreen", True)
        self.label = Label(self, text = (p.byn,p.usd), font=('Arial', 30))
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
        cash = self.entry1.get()
        cash = int(cash)
        while cash > 601 or cash % 5 != 0 or cash == 0:
            self.destroy()
            Withdrawusd().mainloop()
        else:
            p.usd = p.usd - cash
            p.byn = p.usd * 2
            self.enter_sum(cash)
            self.take_of_money_usd(self.sum_take_off)
            self.destroy()
            Question().mainloop()


    def enter_sum(self,cash):
        if 300 < cash < 601:
            a = cash // 100
            b = cash % 100 // 50
            c = cash % 100 % 50 // 20
            d = cash % 100 % 50 % 20 // 10
            e = cash % 100 % 50 % 20 % 10 // 5
        elif 150 < cash < 301:
            a = 0
            b = cash // 50
            c = cash % 50 // 20
            d = cash % 50 % 20 // 10
            e = cash % 50 % 20 % 10 // 5
        elif 60 < cash < 151:
            a = 0
            b = 0
            c = cash // 20
            d = cash % 20 // 10
            e = cash % 20 % 10 // 5
        elif 30 < cash < 61:
            a = 0
            b = 0
            c = 0
            d = cash // 10
            e = cash % 10 // 5
        elif 0 < cash < 31:
            a = 0
            b = 0
            c = 0
            d = 0
            e = cash // 5
        self.sum_take_off = {100: a, 50: b, 20: c, 10: d, 5: e}

        return self.sum_take_off

    def take_of_money_usd(self,sum_take_off):
        all_money = {}
        for key in b.usd:
            balance = b.usd[key] - sum_take_off[key]
            if key not in all_money:
                all_money[key] = balance
        b.usd = all_money



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
        cash = self.entry1.get()
        cash = int(cash)
        while cash > 601 or cash % 5 != 0 or cash == 0:
            self.destroy()
            Withdrawusd().mainloop()
        else:
            p.usd = p.usd - cash
            p.byn = p.usd * 2
            self.enter_sum(cash)
            self.take_of_money_rb(self.sum_take_off)
            self.destroy()
            Question().mainloop()


    def enter_sum(self,cash):
        if 300 < cash < 601:
            a = cash // 100
            b = cash % 100 // 50
            c = cash % 100 % 50 // 20
            d = cash % 100 % 50 % 20 // 10
            e = cash % 100 % 50 % 20 % 10 // 5
        elif 150 < cash < 301:
            a = 0
            b = cash // 50
            c = cash % 50 // 20
            d = cash % 50 % 20 // 10
            e = cash % 50 % 20 % 10 // 5
        elif 60 < cash < 151:
            a = 0
            b = 0
            c = cash // 20
            d = cash % 20 // 10
            e = cash % 20 % 10 // 5
        elif 30 < cash < 61:
            a = 0
            b = 0
            c = 0
            d = cash // 10
            e = cash % 10 // 5
        elif 0 < cash < 31:
            a = 0
            b = 0
            c = 0
            d = 0
            e = cash // 5
        self.sum_take_off = {100: a, 50: b, 20: c, 10: d, 5: e}

        return self.sum_take_off

    def take_of_money_rb(self,sum_take_off):
        all_money = {}
        for key in b.byn:
            balance = b.byn[key] - sum_take_off[key]
            if key not in all_money:
                all_money[key] = balance
        b.byn = all_money
        return b.byn



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
    b = Bankomat()
    p = Person("oleg", 1111, 2000)
    Login().mainloop()
