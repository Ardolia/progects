"""

Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property
и производных от него классов Appartment, Car и CountryHouse.

Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчета налога,
переопределенный в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 ее стоимости,
на машину — 1/200, на дачу — 1/500.

Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.

Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества ,
а затем выдает ему налог на соответствующее имущество и сколько денег ему не хватает (если это так)

"""


class Property:
    def __init__(self, worth, count=100):
        self.worth = worth
        self.count = count

    def calculation(self):
        return self.worth / self.count


class Appartment(Property):
    def __init__(self, worth, count=1000):
        super().__init__(worth, count)


class Car(Property):
    def __init__(self, worth, count=200):
        super().__init__(worth, count)


class CountryHouse(Property):
    def __init__(self, worth, count=500):
        super().__init__(worth, count)


money = int(input('Сколько у Вас денег: '))
sum_tax = 0
is_flat = input('Есть ли у Вас жилье: да/нет ')
if is_flat == 'да':
    worth_flat = int(input('Стоимость жилья: '))
    flat = Appartment(worth_flat)
    sum_tax += flat.calculation()
is_car = input('Есть ли у Вас машина: да/нет ')
if is_car == 'да':
    worth_car = int(input('Стоимость машины: '))
    car = Car(worth_car)
    sum_tax += car.calculation()
is_house = input('Есть ли у Вас дача: да/нет ')
if is_house == 'да':
    worth_house = int(input('Стоимость жилья: '))
    house = CountryHouse(worth_house)
    sum_tax += house.calculation()
if sum_tax < money:
    print('Поздравляю! Вам хватает на погашение налогов:\nСумма налога: {}\nУ Вас останется: {}'.format(
        sum_tax, money - sum_tax
    ))
else:
    print('К сожалению, для уплаты налога в размере {} Вам не хватает {} рублей'.format(
        sum_tax, sum_tax - money
    ))
