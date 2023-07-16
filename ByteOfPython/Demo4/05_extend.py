class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember: {})".format(self.name))

    def tell(self):
        print("name:{}, age:{}".format(self.name, self.age))

# 注意这里:如果要使用继承需要在定义子类时后面跟上一个带有父类的元组
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        # Python不会自动调用基类 SchoolMember 的构造函数，你必须自己显式地调用它
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print("Salary:{}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, grade):
        SchoolMember.__init__(self, name, age)
        self.grade = grade

    def tell(self):
        SchoolMember.tell(self)
        print("Grade:{}".format(self.grade))


t = Teacher('zs', 30, 3000)
s = Student('ls', 20, 2)

members = [t, s]
for member in members:
    member.tell()

