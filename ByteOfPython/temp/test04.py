class Demo:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        print(self.name)


d = Demo(1, 1)
d.get_name()
