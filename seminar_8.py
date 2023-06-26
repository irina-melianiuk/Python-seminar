
# with open('test.txt', 'r', encoding='utf-8') as file:
# text = file.read()
# for letter in text:
# print(letter)

# while True:
# line = file.readline()
# if not line:
# break
# print(line[:-1])
"""
    text = file.read().splitlines()
    print(text)

with open('result.txt', 'w', encoding='utf-8') as file:
    some_list = ['привет', 'пока', 'как дела']
    for word in some_list:
        file.write(word + '\n')

with open('result.txt', 'a', encoding='utf-8') as file:
    some_list = ['привет', 'пока', 'как дела']
    for word in some_list:
        file.write(word + '\n')
"""

# Дан файл с несколькими строчками, пользователь вводит в консоль символ, нужно найти количество
# повторов этого символа во всем файле.
"""
let1=input ('Ведите символ для поиска - ')
count=0
with open('test.txt', 'r', encoding='utf-8') as file:
    text = file.read()

for letter in text:
    if letter == let1:
        count += 1
        print(let1)
        print(count)
"""

# Дан файл следующего формата:
# Фамилия ученика: список оценок через запятую
# Сальников: 5, 5, 2, 3, 5, 5
# Нужно записать в новый файл фамилию ученика и его средний балл через :
# Сальников: 3.5
""""
with open('school1.txt', 'r', encoding='utf-8') as file:
    with open('school2.txt', 'w', encoding='utf-8') as file1:
        text = file.read().splitlines()

        for student in text:
            line=student.split(':')
            name=line[0]
            marks=line[1].split(', ')
            marks=list(map(int,marks))
            rezult=sum(marks)/len(marks)
            file1.write(f'{name}:{round(rezult,1)}\n')
"""
# Дан файл, нужно полностью скопировать его в другой файл
"""
with open('school1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(text1)
"""

