#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Bankomat:
    def __init__(self, id_num, min_withdraw, max_withdraw):
        self.id_num = id_num
        self.min_withdraw = min_withdraw
        self.max_withdraw = max_withdraw
        self.bills = {10: 0, 50: 0, 100: 0, 500: 0, 1000: 0}

    def read(self):
        self.id_num = input("Введите идентификационный номер банкомата: ")
        self.min_withdraw = int(input("Введите минимальную сумму для снятия: "))
        self.max_withdraw = int(input("Введите максимальную сумму для снятия: "))
        for denomination in self.bills:
            self.bills[denomination] = int(input(f"Введите количество купюр номиналом {denomination}: "))

    def display(self):
        print(f"ID банкомата: {self.id_num}")
        print(f"Минимальная сумма для снятия: {self.min_withdraw}")
        print(f"Максимальная сумма для снятия: {self.max_withdraw}")
        print("Количество купюр по номиналам:")
        for denomination, count in self.bills.items():
            print(f"Номинал {denomination}: {count} шт.")

    def load_bills(self, denomination, count):
        if denomination in self.bills:
            self.bills[denomination] += count
        else:
            print(f"Неверный номинал купюр: {denomination}")

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Сумма меньше минимальной суммы для снятия: {self.min_withdraw}")
            return False
        if amount > self.max_withdraw:
            print(f"Сумма превышает максимальную сумму для снятия: {self.max_withdraw}")
            return False

        remaining_amount = amount
        bills_to_dispense = {10: 0, 50: 0, 100: 0, 500: 0, 1000: 0}

        for denomination in sorted(self.bills.keys(), reverse=True):
            if remaining_amount >= denomination:
                num_bills = min(remaining_amount // denomination, self.bills[denomination])
                bills_to_dispense[denomination] = num_bills
                remaining_amount -= num_bills * denomination

        if remaining_amount == 0:
            for denomination in bills_to_dispense:
                self.bills[denomination] -= bills_to_dispense[denomination]
            print(f"Выдано {amount} руб. следующими купюрами: {bills_to_dispense}")
            return True
        else:
            print(f"Невозможно выдать запрашиваемую сумму {amount} руб. текущими купюрами.")
            return False

    def toString(self):
        total_amount = sum(denomination * count for denomination, count in self.bills.items())
        return f"Оставшаяся сумма в банкомате: {total_amount} руб."

if __name__ == '__main__':
    atm = Bankomat("ATM-001", 100, 5000)
    atm.load_bills(1000, 5)
    atm.load_bills(500, 10)
    atm.load_bills(100, 50)
    atm.load_bills(50, 100)
    atm.load_bills(10, 200)

    print(atm.toString())

    atm.withdraw(280)
    print(atm.toString())

    atm.display()