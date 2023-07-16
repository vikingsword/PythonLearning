# 使用 * 定义元组
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
print(powersum(2, 10))


# 使用 ** 定义字典
def powserdict(power, **dict):
    total = 0
    for key, value in dict.items():
        total += pow(value, power)
    return total


dict = {
    'jack': 3,
    'tom': 4
}
print('dict:')
print(powserdict(2, jack=2, tom=3))
