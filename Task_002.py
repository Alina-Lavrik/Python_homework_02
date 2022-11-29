# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from os import system
system("cls")

import math

num = int(input("Введите число: "))
result = [math.factorial(i) for i in range(1, num + 1)]
print(f'Произведений чисел равно: {result}')