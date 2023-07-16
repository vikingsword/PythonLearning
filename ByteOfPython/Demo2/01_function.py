def sayHello():
    print("hello")


def multiNum(a, b):
    print(a * b)


# a is range
def getMaxNumInRange(a):
    for i in a:
        max = i
        if max <= i:
            max = i
    print("the max number in {0} is {1}".format(a, max))


r = range(1, 10)
getMaxNumInRange(r)

print("--------------------")

a = 10


def function1():
    a = 1
    print(a)


print(a)

print("--------------------")


# 注意python局部变量作用域
def function2():
    b = 1
    if b < 10:
        c = 1
    else:
        c = 2
    print(b)
    print(c)


function2()

print("--------------------")

x = 10


def function3():
    global x
    x = 1
    print(x)


function3()
print(x)

print("--------------------")


def sayMessage(num, times=2):
    print(num * times)


sayMessage(3, 4)
sayMessage("hello", 3)
sayMessage("wo")

print("world" * 4)

print("--------------------")


def fun1(a, b=1, c=2):
    print(a + b + c)


fun1(1)
fun1(1, b=2)
fun1(1, b=2, c=4)
fun1(c=3, b=2, a=4)
fun1(4, b=3, c=3)

print("--------------------")


def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(11, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

print("--------------------")


def fun2(number=1, *arr, **double_arr):
    print(number)
    for item in arr:
        print("item ", item)
    for item1, item2 in double_arr.items():
        print("item1 is {0},item2 is {1}".format(item1, item2))


print(fun2(2, 1, 2, 3, tom="12", jerry="5"))

print("--------------------")


def getMinValue(a, b):
    '''Print the minimum number.'''
    # sdfsdfs
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return "equal"


print(getMinValue(1, 2))
print(getMinValue.__doc__)
help(getMinValue)
help(print)