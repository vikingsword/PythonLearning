import pickle

shopListFile = 'shopList.data'
shopList = ['apple', 'mango', 'carrot']

f = open(shopListFile, 'wb')
pickle.dump(shopList, f)
f.close()

del shopList

f = open(shopListFile, 'rb')
storedList = pickle.load(f)
print(storedList)
