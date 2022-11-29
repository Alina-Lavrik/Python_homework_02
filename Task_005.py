# 5. Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint


mix = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Список: {mix}')

for i in range(len(mix)-1):
    n = randint(0, len(mix)-1)
    mix[i], mix[n] = mix[n], mix[i]
print(f'Перемешанный список: {mix}')
