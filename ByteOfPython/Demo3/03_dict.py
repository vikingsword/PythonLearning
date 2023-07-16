# It's similar to map structure in java.
# headers is a dict, easy to remember.
ab = {
    'Swarovski': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

value = ab['Larry']
print(value)

del ab["Larry"]


def printAb():
    for key, email in ab.items():
        print("the {0} of email is {1}".format(key, email))


ab["Viking"] = "bon.voyage.ma.princess@gmail.com"
printAb()

if 'Viking' in ab:
    print("ok")
if 'bon.voyage.ma.princess@gmail.com' in ab:
    print("that's right")

number = {}
for i in range(0, 10):
    number[i] = i * i

for key, value in number.items():
    print('key: ' + str(key) + '\tvalue: ' + str(value))
