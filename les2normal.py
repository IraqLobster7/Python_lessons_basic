
__author__ = 'Барсанов Сергей Сергеевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

number = input("Введите целое число")
list_number = list(number)
i = 1
while i < len(list_number):
    if list_number[i - 1] < list_number[i]:
        max = list_number[i]
    i += 1
print(max)
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
a = int(input('Пожалуйста введите первое число: '))
b = int(input('Пожалуйста введите второе число: '))

a = a + b
b = a - b
a = a - b
print(a, b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
