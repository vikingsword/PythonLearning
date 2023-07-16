animal = ["dog", "cat", "elegant"]
# refer 只是指向同一对象的另一种名称
refer = animal

print(refer)
print(animal)

del animal[0]

print(refer)
print(animal)

print("---------------")

dog = ["name", "age", "breed", "color"]
# 通过生成一份完整的切片制作一份列表的副本
dog_refer = dog[:]
# 如果还是dog_refer = dog 这种形式，del dog_refer之后会将dog和dog_refer都删除

del dog_refer[0]
print(dog_refer)
print(dog)

print("-----------------")

# I think there is nothing difference in copy function and refer
cat = ["name", "habit", "age"]
cat_refer = cat.copy()

print(cat)
print(cat_refer)

del cat_refer[0]
print(cat)
print(cat_refer)
