print('Задача 2 in 1')
import random


def rock_paper_scissors():
    variants = ["Камень", "Ножницы", "Бумага"]

    while True:
        user = input(
            "Выберите действие: \n1. Камень \n2. Ножницы \n3. Бумага\n")
        bot = random.randrange(0, 3)
        if user == "1" or user == "2" or user == "3":
            user = int(user)
            if user == bot:
                print(f"{variants[user - 1]} - {variants[bot]} - ничья")
            elif (user == 1 and bot == 2 or bot == 3) or\
                 (user == 2 and bot == 3) or \
                 (user == 3 and bot == 1):
                print(f"{variants[user - 1]} - {variants[bot]} - Вы выиграли!")
                break
            else:
                print(
                    f"{variants[user - 1]} - {variants[bot]} - Вы проиграли!")
                break
        else:
            print("Такого варианта нет. Попробуйте еще раз! \n")
    print("Игра окончена. Возвращаемся в главное меню\n\n")


def guess_the_number():

    number = random.randint(0, 100)
    print('Мы загадали число от 0 до 99. Попробуй угадать: ')
    try_number = 0
    while True:
        guess = int(input('Введите число: '))
        try_number += 1
        if guess == number:
            print('Вы угадали! Число попыток:', try_number)
            print("Игра окончена. Возвращаемся в главное меню\n\n")
            break
        elif guess < number:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
        else:
            print('Число больше, чем нужно. Попробуйте ещё раз!')


def mainMenu():
    while True:
        print(
            "В какую игру поиграем? Выберие цифру: \n1. Камень, ножницы, бумага\n2. Угадай число"
        )
        game = input()
        if game == "1":
            rock_paper_scissors()
        elif game == "2":
            guess_the_number()
        else:
            print("Такого варианта нет. Попробуйте еще раз\n")


mainMenu()
