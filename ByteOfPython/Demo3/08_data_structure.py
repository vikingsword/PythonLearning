# 列表
shopList = ['a', 'b', 'c']

# 元组
tuple1 = ('a', 'b', 'c')

# 字典
dict1 = {
    'a': 1,
    'b': '2',
    "c": "hhh"
}
for key, value in dict1.items():
    print("key = {0},value = {1}".format(key, value))

# 增加字典中的一个元素的时候,按如下写法即可
dict1['d'] = 'qqq'
keyList = list(dict1.keys())
print('list1 = ', keyList)

valueList = list(dict1.values())
print('valueList = ', valueList)

print("----------------------")

# 序列(非数据结构)
print(shopList[:])
print(shopList[1:3])

# 集合
collection1 = set(['a', 'b', 'c'])
collection2 = {'a', 'b', 'c'}
# 上面的两个集合等效，如果要创建一个空的集合则必须写set，否则为一个字典
for item in collection1:
    # 输出无序
    print(item)

#
