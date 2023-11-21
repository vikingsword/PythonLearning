class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("name = ", self.name)
        print("age = ", self.age)

    def __str__(self):
        print("init str")


if __name__ == '__main__':
    s = Student("zs", 29)
    s.print()
