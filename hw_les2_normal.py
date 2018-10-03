
__author__ =  ' Барсанов Сергей Сергеевич '

import math
import random


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list_numb = [2, -5, 8, 9, -25, 25, 4, 125, -91, 38, -446, 81, 49, 625, 1557504]
print('Список исходных чисел: ', list_numb)
new_list_numb = []
for numb in list_numb:
    if (numb > 0) and (int(math.sqrt(numb)) == math.sqrt(numb)):
        new_list_numb.append(int(math.sqrt(numb)))
print('Список квадратных корней чисел исходного списка,\nесли корень можно извлечь и корень составляет целое число: \n', new_list_numb)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


data1 = '14.09.1901'
data_list = data1.split('.')
months = {
'01': 'января',
'02': 'февраля',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
}
days = {
'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}
for key in days:
    if data_list[0] == key:
        data_list[0] = days[key]

for key in months:
    if data_list[1] == key:
        data_list[1] = months[key]

answer_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + ' ' "года"
print(answer_data)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
elements = int(input('Введите желаемое кол-во случайных чисел в списке '))
my_list = []
for element in range(elements):
    my_list.append(random.randint(-100, 100))
print('Список случайных чисел: ', my_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

#решение А

numbList = [1, 3, 3, 4, 5, 7, 5, 3, 5, 6, 7, 8, 48, 10, 11, -1, -2, -1, -1, 222, 222, 35]
new_numbList = set(numbList)
print('элементы исходного списка без поторений', new_numbList)

#решение Б

next_list = []
for z in numbList:
    if numbList.count(z) == 1:
        next_list.append(z)
print('элементы исходного списка, которые не имеют повторений', next_list)
