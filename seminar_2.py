"""
Задача 1. Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
# """
# n = int(input('КВведите кол-во элементов: '))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input()))
# print(some_list)
# new_list = []
# for elem in some_list:
#     if elem not in new_list:
#         new_list.append(elem)
# print(len(new_list))

"""
19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – положительное число.
"""

# n = int(input('Последовательность из целых чисел: '))
# k = int(input('Число: '))
# s = []
# for i in range(n):
#     s.append(int(input()))
# print(s)
# x = s[:k]
# y = s[k:]
# z = y + x
# print(z)

"""
23. Дан массив, состоящий из целых чисел. Напишите программу, которая 
подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
"""
# n = int(input('КВведите кол-во элементов: '))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input()))
# print(some_list)
# count = 0
# for i in range(1, len(some_list)):
#     if some_list[i] > some_list[i -1]:
#         count += 1
# print(count)
