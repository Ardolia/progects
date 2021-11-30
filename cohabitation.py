import random


class Home:
    def __init__(self, money=100, products=50, cats_eat=30, dirt=0, statistics_money=0, statistics_eat=0, statistics_fur_coat=0):
        self.money = money
        self.products = products
        self.cats_eat = cats_eat
        self.dirt = dirt
        self.statistics_money = statistics_money
        self.statistics_eat = statistics_eat
        self.statistics_fur_coat = statistics_fur_coat

    def __str__(self):
        info = '\nТекущая информация: \nДеньги: {}\nПродукты: {} \nКошачий корм:  {} \nГрязь:{}'.format(
            self.money,
            self.products,
            self.cats_eat,
            self.dirt
        )
        return info

    def live(self):
        self.dirt += 5


    def statistics(self):
        info = '\nВсего денег заработано: {} \nВсего еды съедено: {} \nВсего шуб куплено: {}'.format(
            self.statistics_money,
            self.statistics_eat,
            self.statistics_fur_coat
        )
        return info


class Resident:
    def __init__(self, name, home, satiety=30):
        self.home = home
        self.name = name
        self.satiety = satiety

    def __str__(self):
        info = '\nИмя: {} \nСытость: {}'.format(
            self.name,
            self.satiety
        )
        return info

    def eat(self, eat_count=30):
        if eat_count > self.home.products:
            last = self.home.products
            self.satiety += last
            self.home.products -= last
            self.home.statistics_eat += last
            print(f'\nНедостаточное количество продуктов в доме. {self.name} доел последние {last} еды')
        elif eat_count < 30:
            self.home.products -= eat_count
            self.satiety += eat_count
            self.home.statistics_eat += eat_count
            print(f'\n{self.name} съел {eat_count} еды. Осталось: {self.home.products}')
        else:
            self.home.products -= 30
            self.satiety += 30
            self.home.statistics_eat += 30
            print(f'\n{eat_count} - слишком большая порция. Хватит с {self.name} и 30!')


class Man(Resident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety)
        self.happiness = happiness

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Счастье: {}'.format(
                    self.happiness,
                )
            )
        )
        return info

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} гладит кота')

class Husband(Man):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety)
        self.happiness = happiness

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print(
            f'Уровень счастья {self.name} повысился от игры в компьютер: {self.happiness}')

    def go_to_work(self):
        print(f'{self.name} сходил на работу и заработал денег')
        self.home.money += 150
        self.happiness -= 10
        self.satiety -= 10
        self.home.statistics_money += 150

    def live(self):
        if self.satiety < 30:
            self.eat()
        elif self.home.money < 350:
            self.go_to_work()
        elif self.happiness < 30:
            self.game()
        else:
            self.game()


class Wife(Man):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety)
        self.happiness = happiness

    def shopping(self):
        if self.home.money <= 0:
            print(f'{self.name} не может купить продукты! Нужно заработать денег')
        else:
            self.home.products += 50
            self.home.cats_eat += 20
            self.home.money -= 70
            self.satiety -= 10
            self.happiness -= 10
            print('{} купила продукты! Осталось денег: {}\nПродуктов в холодильнике: {}\nКошачьей еды: {}'.format(
                self.name,
                self.home.money,
                self.home.products,
                self.home.cats_eat
            ))

    def buy_a_fur_coat(self):
        if self.home.money < 350:
            print('Недостаточно денег на шубу. Придется подкопить.')
        else:
            self.home.money -= 350
            self.happiness += 60
            self.satiety -= 10
            self.home.statistics_fur_coat += 1
            print('{} купили шубу. Уровень счастья повысился: {}'.format(self.name, self.happiness))

    def clean(self):
        if self.home.dirt > 100:
            self.home.dirt -= 100
            print('{} занялась уборкой\nУровень грязи в доме: {}'.format(
                self.name,
                self.home.dirt
            ))
        else:
            self.home.dirt = 0
        self.happiness -= 10
        self.satiety -= 10
        print('{} занялась уборкой\nУровень грязи в доме: {}'.format(
            self.name,
            self.home.dirt
        ))

    def live(self):

        if self.satiety < 30:
            self.eat()
        elif self.home.products < 20:
            self.shopping()
        elif self.home.cats_eat < 20:
            self.shopping()
        elif self.happiness < 50:
            if self.home.money > 350:
                self.buy_a_fur_coat()
            else:
                self.pet_the_cat()
        elif self.home.dirt > 50:
            self.clean()
        else:
            self.pet_the_cat()


class Cat(Resident):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety)

    def eat(self, cats_eat_count=10):
        if cats_eat_count > self.home.cats_eat:
            last = self.home.cats_eat
            print(
                f'Недостаточно кошачьего корма. Кот слопал все что осталось - {self.home.cats_eat}\nСытость кота: {self.satiety}')
            self.home.cats_eat = 0
            self.satiety += last * 2
        elif cats_eat_count > 10:
            self.home.cats_eat -= 10
            self.satiety += 20
            print(f'Слишком большая порция для кота. Максимальная порция - 10!\nСытость кота: {self.satiety}')

        else:
            self.home.cats_eat -= cats_eat_count
            self.satiety += cats_eat_count * 2
            print(f'\n{self.name} съел {cats_eat_count} еды. Осталось: {self.home.cats_eat}\nСытость кота: {self.satiety}')

    def tear_wallpaper(self):
        self.satiety -= 10
        self.home.dirt += 5
        print(f'{self.name} скучно. Кот дерет обои.')

    def sleep(self):
        self.satiety -= 10
        print(f'{self.name} спит.')

    def live(self):
        cat_random = random.randint(1, 10)
        if self.satiety < 20:
            self.eat()
        elif cat_random == 1:
            self.tear_wallpaper()
        else:
            self.sleep()


flat = Home()
tom = Husband('Tom', flat)
mary = Wife('Mary', flat)
puppy = Cat('Pussy', flat)
cat = Cat('lili', flat)
for day in range(1, 366):
    print(f'\nДень {day}: \n')
    tom.live()
    mary.live()
    flat.live()
    puppy.live()
    cat.live()
    print(f'\nИтоги дня № {day}')
    print(tom)
    print(mary)
    print(puppy)
    print(cat)
    print(flat)
    if tom.satiety <= 0 or mary.satiety <= 0:
        print(f'Человек {tom.name if tom.satiety <= 0 else mary.name} умер. Игра окончена!')
        break
    if puppy.satiety <= 0:
        print(f'Кот {puppy.name} умер. Игра окончена!')
        break
    if tom.happiness < 10 or mary.happiness < 10:
        print(f'Человек {tom.name if tom.happiness <= 10 else mary.name} умер от депрессии на {day} день. Игра окончена!')
        break

print(flat.statistics())

# зачет!
