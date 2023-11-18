class demo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def print(self):
        print("p1 = ", self.p1)
        print("p2 = ", self.p2)

    def __str__(self):
        return "hello vikingar"


demo1 = demo(1, 2)

demo1.print()

print(demo1)

print('------------')

class demo2:
    def __init__(self, value):
        self.value = value

    def print(self):
        print("value = ", self.value)


demo3 = demo2("vikingar")
demo3.print()