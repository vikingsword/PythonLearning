# It's similar to the array operation or string operation in java.
animal = ['dog', 'cat', 'elegant', 'python']
name = 'vikingar'

print(animal[0], animal[1], animal[2])
print("-----------")
print(animal[1:])
print(animal[1:3])
print(animal[1:-1])
print("------------")
print(name[:])
print(name[1:])
print(name[1:4])
print(name[0:])
print("niemandea")

nickname = 'niemandea'
nickname1 = nickname[nickname.index('e') + 1:]
print(nickname1)

nickname2 = nickname[:nickname.index('m')]
print(nickname2)