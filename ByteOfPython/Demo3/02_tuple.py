# It seems like there is not similar struction in java,maybe a static constant of object?
zoo = ("dog", "cat", "elegant", "python")
new_zoo = ("eagle", "cow", "bird", zoo)
print(len(zoo))
print(len(new_zoo))
print("the animal's number in the new zoo is", len(zoo) + len(new_zoo) - 1)
print(zoo[3])
print(new_zoo[3][0])

print("----------")
# zoo.append("horse")
# print(zoo)
