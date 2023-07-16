class Person:
    # 空的代码块写pass
    pass


p = Person()
print(p)


class Person2:
    def sayHello(self):
        print('hello')


p2 = Person2()
p2.sayHello()

print("---------------------")


class Person3:
    # __init__在对象被实例化的时候运行，其赋值操作类似java中的构造方法赋值
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print('hello', self.name)


p3 = Person3('cat')
p3.sayHello()
Person3('dog').sayHello()