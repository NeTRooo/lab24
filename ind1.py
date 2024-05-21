#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле first должно быть положительным целым числом.")
        if not isinstance(second, (int, float)) or second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите калорийность 100 г продукта (целое положительное число): "))
        if self.first <= 0:
            raise ValueError("Поле first должно быть положительным целым числом.")
        self.second = float(input("Введите массу продукта в килограммах (дробное положительное число): "))
        if self.second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
    
    def display(self):
        print(f"Калорийность 100 г продукта: {self.first} ккал")
        print(f"Масса продукта: {self.second} кг")
    
    def power(self):
        # Калорийность на 100 г умножаем на массу в килограммах и на 10 (так как 1 кг = 1000 г)
        return self.first * self.second * 10

def make_Pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    # Демонстрация возможностей класса Pair
    pair = make_Pair(150, 0.5)  # Создание экземпляра класса Pair
    if pair:
        pair.display()          # Вывод значений полей
        print(f"Общая калорийность продукта: {pair.power()} ккал")  # Вычисление общей калорийности

    print("\nЧтение значений с клавиатуры:")
    pair = Pair(100, 1)  # Создание временного экземпляра для вызова метода read
    pair.read()          # Чтение значений с клавиатуры
    pair.display()       # Вывод значений полей
    print(f"Общая калорийность продукта: {pair.power()} ккал")  # Вычисление общей калорийности
