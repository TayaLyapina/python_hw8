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

phonebook = {'Иванов Иван Иванович': ['+79521111111', '14.02.2000', 'mail@mail.ru'], 'Петрова Юлия':['+78524444444', '*', 'gmail@gmail.com']}

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
    if name == '*' or name.isalpha():
        return name
    elif not name.isalpha():
        print('Некорректный ввод')
        name = input('Введите имя контакта: ')
        correct_contact_name(name)

def correct_number(text):
    while True:
        if text[0] == '+' and text[1:].isdigit() and len(text) == 12:
            return text
        print('не корректный ввод')
        text = input('Введите номер +7 код номер без пробелов: ')
        correct_number(text)

def correct_birthday(text):
    '''проверка даты рождения'''
    if len(text.split('.')) == 3:
        try:
            datetime.datetime.strptime(text, '%d.%m.%Y')
            return text
            
        except Exception:
            print('неверный формат')
            text = input('Введите дату рождения контакта в формате дд.мм.гггг либо * : ')
            correct_birthday(text)
   
def correct_mail(text):
    '''проверка email'''
    while True:
        for i in range(len(mail)):
            if mail[i] == '@' and '.' in mail[i:]:
                return mail
        print('Укажите корректный email адрес.')
        mail = input(f'{text} > ')

def add_new_contact():
    data = load_phonebook(phonebook)
    contact = ''
    print('Введите данные контакта')
    contact_surname = input('Введите фамилию контакта: ')
    is_correct = correct_contact_name(contact_surname)
    contact_name = input('Введите имя контакта: ')
    is_correct = correct_contact_name(contact_name)
    if is_correct:
        contact = contact_surname.title() + ' ' + contact_name.title()
        print(contact)
        if contact in data.keys():
            print('Данный контакт существует')
        else:
            contact_details = []
            contact_number = input('Введите номер +7 код номер без пробелов: ')
            is_correct = correct_number(contact_number)
            contact_details.append(contact_number)
            contact_birthday = input('Введите дату рождения контакта в формате дд.мм.гггг либо * : ')
            is_correct = correct_birthday(contact_birthday)
            contact_details.append(contact_birthday)
            contact_mail = input('Введите email контакта либо * : ')
            is_correct = correct_birthday(contact_mail)
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
                is_correct = correct_number(contact_number)
                contact_new_details.append(contact_number)
            elif a == 'n':
                contact_number = contact_old_details[0]
                contact_new_details.append(contact_number)
            a1 = input('Вы хотите изменить дату рождения? y/n \n')
            if a1 == 'y':
                contact_birthday = input('Введите дату рождения контакта в формате дд.мм.гггг либо * : ')
                is_correct = correct_birthday(contact_birthday)
                contact_new_details.append(contact_birthday)
            elif a1 == 'n':
                contact_birthday = contact_old_details[1]
                contact_new_details.append(contact_birthday)
            a2 = input('Вы хотите изменить email? y/n \n')
            if a2 == 'y':
                contact_mail = input('Введите email контакта либо * : ')
                is_correct = correct_birthday(contact_mail)
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