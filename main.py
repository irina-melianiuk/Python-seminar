"""
# 1. Сумма трех
# Посчитатйте сумму трех введенных целых чисел

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Сумма трех числе равна:', a + b + c)
"""
"""
# 2. Площадь круга.
# Пользователь вводит радиус круга, выведите площадь круга.

r = int(input('Введите радиус круга: '))
print(f'Площадь круга с радиусом {r} равна ', r * r * 3.14 )
"""

# 3. Четырехзначное
# Пользователь вводит целое число. Выведите YES, если число является четырехзначным и NO в противном случае.
"""
a = int(input('Введите число: '))
if (a >= 1000 and a <= 9999) or (a <= -1000 and a >= -9999):
   print('YES')
else:
   print('NO')
"""    
"""
a = input('Введите число: ')
if len(a) == 4:
    print('YES')
else:
   print('NO')
"""
"""
a = int(input('Введите число: '))
if a < 0:
    if len(str(a)) == 5:
         print('YES')
    else:
         print('NO')
else :
     if (a >= 1000 and a <= 9999) or (a <= -1000 and a >= -9999):
         print('YES')
     else:
         print('NO')
"""

# 4. Описание числа
# Пользователь вводит целое число. Выведите его строку-описание вида отрицательное четное число, ноль, положительное нечетное число.
# например, численное описание числа 190 является строка "поло;ительное четное число"
"""
a = int(input('Введите число: '))
if a < 0:
    znak = 'отрицательное'
else :
    znak = 'положительное'
if a % 2 == 0:
    chetnost = 'четное'
else :
    chetnost = 'не четное'
print(f'Численное описание числа {a} является: ', znak, chetnost, 'число')
"""

# 5. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длинной m километров?
# при решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
"""
n = int(input('Введите количество километров за день: '))
m = int(input('Введите общее количество километров: '))
m = -m
res = -(m//n)
print(res)
"""

""" 6. В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них"""
"""
n1 = int(input('Введите количество учеников в 1 классе: '))
n2 = int(input('Введите количество учеников во 2 классе: '))
n3 = int(input('Введите количество учеников в 3 классе: '))
desk = (n1 // 2 + n1 % 2) + (n2 // 2 + n2 % 2) + (n3 // 2 + n3 % 2)
print(f'Необходимо купить {desk} парт.')
"""

# 7. Вагоны в элеткричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от голвы, а иногда и хвоста. 
# все засит в какую сторону едет поезд.) В каждом вагоне написан номер вагона. Витя сел в i-тый ваго от головы поезда и обнаружил номер j.
# Он хочет определить, сколько вагонов всего в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# 8. Дано натральное число. Требуется определить, является ли год с данным номером высокосным. Если год является высокосным, то выведите YES, иначе NO.
# Напомним, что в соответсвтии с григорианским календарем, год является высикосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
"""
year = int(input('Введите год: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print('YES')
else:
   print('NO')
"""
# СЕМИНАР НОМЕР 2
"""
# Вводятся числа, пока не введут 0. Найти произведение чисел, оканчивающихся на 4
"""
# mult = 1
# number = int(input())
# while number != 0 :
#     if number % 10 == 4 :
#         mult *= number
#     number = int(input())
# if mult == 1 :
#     milt = 0
# print(mult)

""" 
# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введенного слова
равна 5, то нужно вывести сообщение YES и прекратить возможность ввода для пользователя? если таких слов нет, то вывести NO оин раз в конце.
"""
# flag = True
# while True:
#     some_str = input()
#     # if some_str == '':
#     #     break
#     if not some_str:
#         break
#     if len(some_str) == 5:
#         print('YES')
#         flag = False
#         break
# if flag :
#     print('NO')

# другое решение
# some_str = input()
# while some_str:
#     if len(some_str) == 5:
#         print('YES')
#         break
#     some_str = input()
# else :
#     print('NO')


# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# Переменная итератор используется внутри цикла
# for i in 'hello':
#     print(i)

# for j in 1, 2, 3, 4, 5:
#     print(** 2)

# range()
# for number in range(1, 11): 1.2.3.4....10
#     print(number)

# for number in range(5): 0.1.2.3.4
#       print(number)

# for number in range(2, 101, 2): #всее четные от 2 до 100
#     print(number, end=' ')

# for number in range(10, 1, -2): от 10 до 2 все четные
#     print(number)

# Переменная итератор не используется внутри цикла
# 100 раз вывести слово hello в консоли

# for _ in range (100): # 0 1 2 3 4 5 .... 99
#     print('HELLO')

# Введите количество чисел,затем сами числа, енайти сумму чисел, кратных 3

# n = int(input('Введите количество чисел: ')) #10
# summa= 0
# for _ in range(n): # 0 1 2 3 ... 9
#     number = int(input())
#     if number % 3 == 0:
#         summa += number
# print(summa)

# Введите количество чисел,затем сами числа, если число = 10, вывести да и закончить ввод, в конце вывести нет если никакое из чисел не было равно 10

# n = int(input('Введите количество чисел: ')) #10
# # flag = True
# for _ in range(n): # 0 1 2 3 ... 9
#     number = int(input())
#     if number == 10:
#         print('YES')
#         # flag = False
#         break
# else:
#     print('NO')
    


"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""
# n = int(input('Введите N: '))
# res = 1
# i = 1
# while i <= n : # 1 2 3 4 5
#     res *= i
#     i += 1
# print(res)

"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""
# a = int(input('Введите значение: '))
# if a == 0:
#     print(0)
# else:
#     first = 0
#     second = 1
#     third = first + second
#     count = 3
#     while third < a:
#         first = second
#         second = third
#         third = first + second
#         count += 1
#     if third == a:
#         print(count)
#     else:
#         print(-1)


"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""
# num_day = int(input('Введите общее количество рассматриваемых дней: '))
# max_count = 0
# temp_count = 0
# for _ in range(num_day):
#     temperature = int(input('Введит температуру: '))
#     if temperature >= 0:
#         temp_count += 1
#     else:
#         temp_count = 0
#     if temp_count > max_count:
#         max_count = temp_count
# print(max_count)

"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
# watermelons = int(input('Введите кол-во арбузов:'))
# max_kg = int(input('Введите массу арбуза:'))
# min_kg = max_kg
# for _ in range(watermelons - 1):
#     weight = int(input('Введите массу арбуза:'))
#     if weight > max_kg:
#         max_kg = weight
#     else:
#         if weight < min_kg:
#             min_kg = weight
# print(max_kg, min_kg)