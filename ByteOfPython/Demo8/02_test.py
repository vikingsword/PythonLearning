class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('zs', 12)
print(p.name, p.age)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Animal:
    def __init__(self, name, age):
        self.name = name
        # self.age2 = age

    def getName(self):
        print(self.name)


print('----------------')
a = Animal('dog', 12)
a.getName()
