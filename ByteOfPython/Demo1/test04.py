num = 5
count = 1
while count <= 10:
    guess = int(input("please input a number: "))
    if num == guess:
        print("guess right")
    elif num < guess:
        if True:
            print("hello this is ture")
        print("password is smaller")
    else:
        print("password is bigger")
    count += 1
print("Done")