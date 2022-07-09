class Eletric:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        self.on = False

    def turn_on(self):
        if self.on is True:
            self.on = False
        else:
            self.on = True

    def __str__(self):
        return f"{self.name}"


class Pessoa:
    def __init__(self, name, account_money):
        self.name = name
        self.own_eletronics = []
        self.__account_money = account_money

    def buy_eletronic(self, eletronic: Eletric):
        if self.__account_money >= eletronic.price:
            self.__account_money -= eletronic.price
            self.own_eletronics.append(eletronic.name)
        else:
            return "Doesnt have money for this product"

    def show_eletronics(self):
        return self.own_eletronics


class Refrigerator(Eletric):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)

    def __str__(self):
        return f"{self.name}"


person = Pessoa('Alef', 4000)
refrigerator = Refrigerator('Refrigerator', 'Black', 2000)

print(person.show_eletronics())
person.buy_eletronic(refrigerator)
print(person.show_eletronics())

print(refrigerator.on)
refrigerator.turn_on()
print(refrigerator.on)
