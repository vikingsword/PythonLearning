# b = True
# password = 6
# while b:
#     guess = int(input("please input right number: "))
#     if password == guess:
#         b = False
# print("Done!")

# python code is graceful!!!
for i in range(1, 5):
    print("this is " + str(i))
else:
    print("Done!")

print("--------------------")

for i in range(1, 5, 2):
    print("this is " + str(i))
else:
    print("Done!")

print("--------------------")

array = list(range(1, 5))
print(array)

print("--------------------")

list = range(1, 5)
print(list)

print("--------------------")

for j in range(0, 5):
    if j == 3:
        print(j)
        break
print(j)

print("--------------------")

while True:
    s = input("input something on console: ")
    if s == "quit":
        print("game over!")
        break
    elif len(s) < 3:
        print("the length is too short!")
        continue
    print("if your input length shorter than three this word is not be excute")
