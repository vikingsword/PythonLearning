class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember :{})".format(self.name))

    def tell(self):
        print('name:{},age: {}'.format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, grade):
        SchoolMember.__init__(self, name, age)
        self.grade = grade

    def tell(self):
        SchoolMember.tell(self)
        print("Grade: {}".format(self.grade))


t = Teacher('zs', 30, 3000)
s = Student('ls', 20, 1)

members = [t, s]
for member in members:
    member.tell()
