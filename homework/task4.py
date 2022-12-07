# 1. Вычислить число Пи c заданной точностью d
#    *Пример:* 

#    - при d = 0.001, π = 3.141
#    - при d = 0.0001, π = 3.1415  

import math
from math import pi

n = pi
# print(n)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#    * 6 -> [1,2,3]
#    * 144 -> [2,3]

num = int(input("Введите число: "))
i = 2 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа : {lst}")

# 3. Задайте последовательность чисел. Напишите программу,
#    которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
#    k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. Даны два файла, в каждом из которых находится запись многочлена. 
#    Задача - сформировать файл, содержащий сумму многочленов.
#    В file1.txt :
#    2*x**2 + 4*x + 5
#    В file2.txt:
#    4*x**2 + 1*x + 4
#    Результирующий файл:
#    6*x**2 + 5*x + 9

import random


def write_file(st):
    with open('file3.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))







