def menu():
    print(
        "Квест - выйди из квартиры! \nВ квартире есть три комнаты (спальня, кухня, ванна) и коридор. Ваша задача - выбраться на улицу! Выберите, из какой комнаты начнем игру:\n1. Спальня \n2. Кухня \n3. Ванна \n"
    )
    while True:
        choice = input("Ваш выбор: ")
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            if choice == 1:
                bedroom()
            elif choice == 2:
                kitchen()
            elif choice == 3:
                bathroom()
        else:
            print("Такого варианта нет. Попробуйте еще раз.\n")


def bedroom():
    print("Вы в спальне. Куда идем?\n1. Коридор \n2. Ванна \n")
    while True:
        choice = input("Ваш выбор: ")
        if choice == "1" or choice == "2":
            choice = int(choice)
            if choice == 1:
                corridor()
            elif choice == 2:
                bathroom()
        else:
            print("Такого варианта нет. Попробуйте еще раз.\n")


def kitchen():
    print("Вы на кухне. Куда идем?\n1. Коридор \n2. Выходим в окно \n")
    while True:
        choice = input("Ваш выбор: ")
        if choice == "1" or choice == "2":
            choice = int(choice)
            if choice == 1:
                corridor()
            elif choice == 2:
                print(
                    "К сожалению, вы были слишком высоко и разбились. Игра окончена!"
                )
                gameOver()
        else:
            print("Такого варианта нет. Попробуйте еще раз.\n")
    pass


def bathroom():
    print("Вы в ванне. Куда идем?\n1. Коридор \n2. Спальня \n")
    while True:
        choice = input("Ваш выбор: ")
        if choice == "1" or choice == "2":
            choice = int(choice)
            if choice == 1:
                corridor()
            elif choice == 2:
                bedroom()
        else:
            print("Такого варианта нет. Попробуйте еще раз.\n")


def corridor():
    print(
        "Вы в коридоре. Куда идем?\n1. Кухня \n2. Спальня \n3. Ванна \n4. Выход \n"
    )
    while True:
        choice = input("Ваш выбор: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            choice = int(choice)
            if choice == 1:
                kitchen()
            elif choice == 2:
                bedroom()
            elif choice == 3:
                bathroom()
            elif choice == 4:
                exit()

        else:
            print("Такого варианта нет. Попробуйте еще раз.\n")


def gameOver():
    print(
        "\n= = = = = = = = = = = = = = \n\n    G A M E  O V E R !   \n\n= = = = = = = = = = = = = = \n"
    )
    menu()


def exit():
    print(
        "\n* * * * * * * * * * * * * * * *  \n\n    П О З Д Р А В Л Я Ю !\nВы смогли выбраться из квартиры! \n\n* * * * * * * * * * * * * * * *\n"
    )
    menu()


menu()
