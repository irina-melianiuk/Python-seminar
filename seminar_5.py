"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

"""
n = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(n):
    list_1.append(int(input('Введите значения: ')))
print(list_1)
max = list_1[0]
min = list_1[0]
for i in range(1, len(list_1)):
    if list_1[i] > max:
        max = list_1[i]
    if list_1[i] < min:
        min = list_1[i]
print(max, min)
for i in range(len(list_1)):
    if list_1[i] == max:
        list_1[i] = min
print(list_1)
"""

"""