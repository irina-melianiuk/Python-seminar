"""
Создать телефонный справочник возможностью добавления записей и чтения. Пользователь также может ввести фамилию,
тогда программа должны вывести на экран все записи с этой фамилий.
Также пользователь может добавлять новых людей в справочник в режиме экспорт.

"""
def search():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите фамилию: ')
        for i in book:
            if temp in i:
                print(i)



def new_number():
    surname = input('Введите фамилию: ')
    name = input('Введите имя и отчество: ')
    phone = input('Введите номер телефона: ')
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'\n{surname}\n{name}\n{phone}')


mode = int(input('Введите режим: 1 - Поиск по справочнику, 2 - Добавление новой записи '))

if mode == 1:
    print(search())
elif mode == 2:
    print(new_number())
else:
    print('Некорректный режим')

