class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("I can eat")


class Tigger(Animal):
    def __init__(self, name, age, weight):
        Animal.__init__(self, name, age)
        self.weight = weight

    def eat(self):
        print("I eat meat")


class Cow(Animal):
    def __init__(self, name, age, sex):
        Animal.__init__(self, name, age)
        self.sex = sex

    def eat(self):
        print("I eat grass")


t = Tigger('big cat', 10, 200)
c = Cow('sample', 12, 'female')

animals = [t, c]
for animal in animals:
    animal.eat()
