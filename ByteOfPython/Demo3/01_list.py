# It's similar to arrayList structure in java.
myList = ['apple', 'strawberry', 'banana', 'mango']
for i in myList:
    print(i, end=' ')
print(len(myList))

myList.append("orange")

myList.sort()
print(myList)

oldItem = myList[0]
del myList[0]
print(myList)
print(oldItem)

print("------------------------")
