# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1= int(input("Enter the value of the first element:"))
# d=int(input("Enter the difference of the elements:"))
# n=int(input("Enter the number of items:"))
# res = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*res)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)