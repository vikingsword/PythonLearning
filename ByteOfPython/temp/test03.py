class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("name = ", self.name)
        print("age = ", self.age)


if __name__ == '__main__':
    s = Student("zs", 29)
    s.print()
