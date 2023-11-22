class Demo:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        print(self.name)


d = Demo(1, 1)
d.get_name()

print('-----------')


class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello,	how	are	you?')

    def say_my_name(self):
        print('my name is', self.name)


p = Person("Heisenberg")
p.say_hi()
p.say_my_name()


