import json
import datetime

path = 'phonebook.json'
welcome = ('''
Команды для работы со справочником: 
Просмотр всех записей справочника - 1
Добавление новой записи в справочник - 2
Поиск необходимого контакта - 3
Изменение контакта в справочнике - 4
Удаление контакта из справочника - 5
Выход из программы - q 
''')

phonebook = {'Иванов Иван': ['+79521111111', '14.02.2000', 'mail@mail.ru'], 'Петрова Юлия':['+78524444444', '*', 'gmail@gmail.com']}

def save_phonebook(data: dict, file_name='phonebook.json'):
    with open(file_name, "w", encoding="utf-8") as s:
        json.dump(data, s, ensure_ascii=False, indent=4)



def load_phonebook(data: dict, file_name='phonebook.json'):
            with open(file_name, 'r', encoding='utf-8') as r:  
                data = json.load(r)  
                return data

def print_phonebook():
    'Печать справочника'
    data = load_phonebook(phonebook)
    print()
    for k, v in data.items():
            print(k, ':', v)
    print()

def search_contact():
    'Поиск контакта'
    data = load_phonebook(phonebook)
    contact = input('Введите имя контакта для поиска: ').lower()
    for k, v in data.items():
        if contact == k.lower():
            print(k,':', v)
            return k, True
    else:
        print("Такого контакта не существует")


def correct_contact_name(name: str):
    while True:
        if name == '*' or name.isalpha():
            return name
        else:
            print('Некорректный ввод')
            name = input('Введите имя контакта: ')
            correct_contact_name(name)

def correct_contact_surname(name: str):
    while True:
        if name == '*' or name.isalpha():
            return name
        else:
            print('Некорректный ввод')
            name = str(input('Введите имя фамилию: '))
            correct_contact_surname(name)


def correct_number(text):
    while True:
        if text[0] == '+' and text[1:].isdigit() and len(text) == 12:
            return text
        print('не корректный ввод')
        text = input('Введите номер +7 код номер без пробелов: ')
        correct_number(text)

def correct_birthday(text:str):
    '''проверка даты рождения'''
    # if len(text.split('.')) == 3:
    #     try:
    #         datetime.datetime.strptime(text, '%d.%m.%Y')
    #         return text
            
    #     except Exception:
    #         print('неверный формат')
    #         text = input('Введите дату рождения контакта в формате дд.мм.гггг либо * : ')
    #         correct_birthday(text)
    while True:
        if len(text) == 8 and text.isdigit() or text == '*':
            return text
        else:
            text = input('Введите дату рождения контакта в формате ддммгггг либо * : ')
            correct_birthday(text)


def correct_mail(text):
    '''проверка email'''
    while True:
        if text == '*':
            return text
        elif text != '*':
            for i in range(len(text)):
                if text[i] == '@' and '.' in text[i:]:
                    return text
        print('Укажите корректный email адрес.')
        text = input('Введите email контакта или *: ')
        correct_mail(text)


def add_new_contact():
    data = load_phonebook(phonebook)
    contact = ''
    print('Введите данные контакта')
    contact_surname = input('Введите фамилию контакта: ')
    correct_surname = correct_contact_surname(contact_surname)
    contact_name = input('Введите имя контакта: ')
    correct_name = correct_contact_name(contact_name)
    contact = correct_surname.title() + ' ' + correct_name.title()
    if contact in data.keys():
        print('Данный контакт существует')
    else:
        contact_details = []
        contact_number = input('Введите номер +7 код номер без пробелов: ')
        contact_number = correct_number(contact_number)
        contact_details.append(contact_number)
        contact_birthday = str(input('Введите дату рождения контакта в формате ддммгггг либо * : '))
        contact_birthday = correct_birthday(contact_birthday)
        if contact_birthday != '*':
            contact_birthday = contact_birthday[:2]+'.'+contact_birthday[2:4]+'.'+contact_birthday[4:]
        contact_details.append(contact_birthday)
        contact_mail = str(input('Введите email контакта либо * : '))
        contact_mail = correct_mail(contact_mail)
        contact_details.append(contact_mail)
        phonebook[contact] = contact_details
        save_phonebook(phonebook)
        print()
        print("Контакт успешно добавлен!")

def delete_contact():
    'Удаление контакта целиком'
    data = load_phonebook(phonebook)
    contact = input('Введите имя контакта: ')
    for k in data.keys():
        if contact.lower() == k.lower():
            del data[k]
            save_phonebook(data)
            print('Контакт успешно удален')
            break    
    else:
        print("Такого контакта не существует")

def change_contact():
    data = load_phonebook(phonebook)
    contact = input('Введите имя контакта, который необходимо изменить: ')
    for k in data.keys():
        if contact.lower() == k.lower():
            contact_old_details = data[k]
            contact_new_details = []
            a = input('Вы хотите изменить номер телефона? y/n \n')
            if a == 'y':
                contact_number = input('Введите номер +7 код номер без пробелов: ')
                contact_number = correct_number(contact_number)
                contact_new_details.append(contact_number)
            elif a == 'n':
                contact_number = contact_old_details[0]
                contact_new_details.append(contact_number)
            a1 = input('Вы хотите изменить дату рождения? y/n \n')
            if a1 == 'y':
                contact_birthday = str(input('Введите дату рождения контакта в формате ддммгггг либо * : '))
                contact_birthday = correct_birthday(contact_birthday)
                if contact_birthday != '*':
                    contact_birthday = contact_birthday[:2]+'.'+contact_birthday[2:4]+'.'+contact_birthday[4:]
                contact_new_details.append(contact_birthday)
                
            elif a1 == 'n':
                contact_birthday = contact_old_details[1]
                contact_new_details.append(contact_birthday)
            a2 = input('Вы хотите изменить email? y/n \n')
            if a2 == 'y':
                contact_mail = str(input('Введите email контакта либо * : '))
                contact_mail = correct_mail(contact_mail)
                contact_new_details.append(contact_mail)
            elif a2 == 'n':
                contact_mail = contact_old_details[2]
                contact_new_details.append(contact_mail)
            phonebook[k] = contact_new_details
            save_phonebook(phonebook)
            print()
            print("Контакт успешно изменен!")
            break
    else:
        print("Такого контакта не существует")


action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_phonebook()
    elif action == '2':
        add_new_contact()
    elif action == '3':
        search_contact()
    elif action == '4':
        change_contact()
    elif action == '5':
        delete_contact()