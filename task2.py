# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#    Пример:
#    - 6782 -> 23
#    - 0,56 -> 11

print('Введите вещественное число:')
a = int(input())
sum = 0

while a != 0:
    sum += a % 10
    a = a // 10
print('Сумма цифр:', sum)

# # 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# #    *Пример:*
#    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4

import math

n = int(input('Введите число:'))
multiplications = [math.factorial(i) for i in range(1, n+1)]
print(f'Произведение чисел от 1 до {n}: {multiplications}') 

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#    *Пример:*

#    - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('Введите число:'))
multiplications = [(1+1/i)**i for i in range(1, n+1)]
print(f'Список из N чисел: {multiplications}')
print(f'Сумма N чисел: {sum(multiplications)}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#    Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
#    в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
#    -2 -1 0 1 2 
#    Позиции: 0,1 -> 2

with open('file.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))

n = int(input())
list_gen = [i for i in range(-n, n+1)]
multi = 1
for pos in positions:
    multi *= list_gen[pos]
print(positions)
print(list_gen)
print(multi)

# 5. Реализуйте алгоритм перемешивания списка.

from random import shuffle
from random import randint

mass = list(map(int, input('Введите список:').split()))
print(f'Изначальный список: {mass}')
shuffle(mass)

for i in range(len(mass)-1):
    n = randint(0, len(mass)-1)
    mass[i], mass[n], mass[i]
print(f'Перемешанный список: {mass}')

