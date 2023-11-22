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
    def say_hi(self):
        print('Hello,	how	are	you?')


p = Person()
p.say_hi()