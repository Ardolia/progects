"""
Напишите программу, которая бесконечно запрашивает у пользователя действие,
которое он хочет совершить: добавить контакт или найти человека в списке
контактов по фамилии.

Действие “добавить контакт”: программа запрашивает имя и фамилию контакта,
затем номер телефона, после этого добавляет их в словарь и выводит на
экран текущий словарь контактов. Если этот человек уже есть в словаре,
то выведете соотвествующее сообщение.

Действие “поиск человека по фамилии”: программа запрашивает фамилию и
выводит все контакты с такой фамилией и их номера телефонов.
Поиск не должен зависеть от регистра символов.
"""

def add_contact(name, surname, phone_number):
    result_search = False
    for key in phones_book.keys():
        if (surname, name) == key:
            print("Такой человек уже есть в словаре!")
            result_search = True
    if not result_search:
        phones_book[surname, name] = phone_number
        print("Запись успешно добавлена.")
        print("Словарь обновлен: \n")
        for key, value in phones_book.items():
            print("\t", " ".join(list(key)), ":", value)


def search(surname):
    result = False
    for key, value in phones_book.items():
        if surname in key:
            result = True
            print("\t", " ".join(list(key)), ":", value)
    if not result:
        print("Такого человека в списке контактов.")


phones_book = {
    ("Иванов", "Иван"): "892061311414",
    ("Кузнецова", "Клавдия"): "89209991291",
    ("Кузнецова", "Анна"): "90000394022"
}

while True:
    action = input("\nВыберите действие: \n1. Добавить контакт\n2. Поиск человека по фамилии\nВаш выбор: ")
    if action == "1":
        print("\nДобавление нового контакта. Введите следующие данные: ")
        name = input("Имя: ").capitalize()
        surname = input("Фамилия: ").capitalize()
        phone_number = input("Номер телефона: ")
        add_contact(name, surname, phone_number)
    elif action == "2":
        print("\nПоиск человека по фамилии")
        find_surname = input("Введите фамилию: ").capitalize()
        search(find_surname)
