mylist = ['item']
assert len(mylist) >= 1

value = mylist.pop()
print(value)

animals = ['dog', 'cat', 'elegant']
print(animals.pop())

tuple = ('dog', 'cat', 'python', 'elegant')
print('tuple = ', tuple)
tuple2 = (i + '.meat' for i in tuple if len(i) > 3)
print('tuple2 = ', tuple2[0, 2])

assert len(animals) >= 2
