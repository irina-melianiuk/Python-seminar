"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

"""
"""
n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)
x = int(input('Введите искомый элемент: '))
count = 0
for i in range(1, len(some_list)):
    if some_list[i] == x:
        count += 1
print(f'Число {x} встречается {count} раз')
"""


"""
Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
"""
n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)
x = int(input('Введите искомый элемент: '))
min_difference = x - some_list[0]
index = 0
for i in range(1, len(some_list)):
    count = x - some_list[i]
    if 0 < count < min_difference:
        min_difference = count
        index = i
print(f'Самый близкий по величине элемент к числу {x} является {some_list[index]}.')
"""
