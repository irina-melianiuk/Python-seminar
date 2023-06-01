# МНОЖЕСТВА
# import random
# import time
#
# some_set = set()
# for _ in range(10 ** 6):
# some_set.add(random.randint(100, 1100))
# some_list = list(some_set)
#
# start = time.perf_counter()
# print(99 in some_list)
# end = time.perf_counter()
# first_duration = end - start
#
# start = time.perf_counter()
# print(99 in some_set)
# end = time.perf_counter()
# second_duration = end - start
# print(first_duration / second_duration)

# СЛОВАРИ
"""
some_dict = {'яблоко': 'apple', 'виноград': 'grape', 'банан': 'ban'}
some_dict['банан'] = 'banana'
print(some_dict['виноград'])

for i in some_dict:
print(i, some_dict[i])

for j in some_dict.values():
print(j)

for i in sorted(some_dict):
print(i, some_dict[i])
"""
"""
Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D,
G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

*Пример:*

ноутбук
12
'''
"""
# scrabble_dict = {1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P', 4: 'F, H, V, W, Y'}
# some_str = input()
# summa = 0
#
# for letter in some_str:
# for key in scrabble_dict:
# if letter in scrabble_dict[key]:
# summa += key
# print(summa)

# scrabble_dict = {'A': 1, 'E': 1, 'I': 1}
# some_str = input()
# summa = 0
#
# for letter in some_str:
# summa += scrabble_dict[letter]
# print(summa)
                 


"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()

"""
# 25. Напишите программу, которая принимает на вход строку,
# и выводит на экран кол-во повторений каждого из символов

# Ввод: как дела
"""k - 2
а - 2
д - 1
е - 1
л - 1
"""
"""
string = input("Введите строку: ")
counts = {} # Создаем словарь

for letter in string:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

for letter, count in counts.items():
    print("Символ '{}' повторяется {} раз(а)".format(letter, count))
"""
"""
string = input("Введите строку: ")
dict = {}

for item in string:
    dict[item] = dict.get(item, 0) + 1

for item, count in dict.items():
    print(f"Символ '{item}' встречается {count} раз(а)")
"""
some_dict = {}
word = input()
for letter in word:
    if letter not in some_dict:
        some_dict[letter] = 1
    else:
        some_dict[letter] += 1
print(some_dict)
"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
"""

"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)
Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""