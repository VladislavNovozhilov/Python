# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#    *Пример:*

#    [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# mass = [2, 3, 5, 9, 3]
# summ = 0
# for i in range(1, len(mass), 2):
#     if i % 2 == 1:
#         summ += mass[i]       
# print(f'{mass} -> сумма элементов на нечётных позициях: {summ}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    *Пример:*

#    [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
#    [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, 
#    которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#    *Пример:*

#    [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# new_lst = [round(i%1,2) for i in lst]
# print(lst, '=>', max(new_lst) - min(new_lst))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    *Пример:*

#    45 -> 101101
#    3 -> 11
#    2 -> 10

# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

