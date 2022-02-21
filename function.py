from tkinter import *


class Bankomat():

    def __init__(self):
        self.byn = {100: 500, 50: 500, 20: 500, 10: 500, 5: 500}
        self.usd = {100: 500, 50: 500, 20: 500, 10: 500, 5: 500}


class Person():
    def __init__(self, name, pin, byn):
        self.name = name
        self.pin = pin
        self.byn = byn
        self.usd = byn / 2


def test_sum():
    cash = entry.get()
    cash = int(cash)
    while cash > 601 or cash % 5 != 0 or cash == 0:
        cash = entry.get()
        cash = int(cash)
    return cash


def enter_sum(cash):
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
    sum_take_off = {100: a, 50: b, 20: c, 10: d, 5: e}

    return sum_take_off


def take_of_money_rb(sum_take_off):
    all_money = {}
    for key in b.byn:
        balance = b.byn[key] - sum_take_off[key]
        if key not in all_money:
            all_money[key] = balance
    b.byn = all_money
    return b.byn


def take_of_money_usd(sum_take_off):
    all_money = {}
    for key in b.usd:
        balance = b.usd[key] - sum_take_off[key]
        if key not in all_money:
            all_money[key] = balance
    b.usd = all_money
    return b.usd


def main():
    cash = test_sum()
    sum_take_off = enter_sum(cash)
    take_of_money_rb(sum_take_off)
    print(b.byn)
    print(p.byn - cash)
    label['text'] = (p.byn - cash)
    p.usd = (p.byn - cash) / 2







