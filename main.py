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

