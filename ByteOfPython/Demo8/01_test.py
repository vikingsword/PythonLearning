pizza = {'crust': 'thick', 'topping': ['mushrooms', 'extra cheese']}

for a, ba in pizza.items():
    print('\nkeys: ', a)
    if isinstance(ba, list):
        for b in ba:
            print('value: ', b)
    else:
        print('value: ', ba)

