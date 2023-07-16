# 持久化对象
import pickle

animalList = ['dog', 'cat', 'elegant', 'tigger']
targetFile = '04_backup.txt'

# 使用open函数打开一个文件,需要指定文件名,默认模式为read(r),可以指定为write(w)
# 默认以文本的方式写入文件(t),可以指定以二进制方式写入文件(b)
# 这里只能用二进制方式写入文件
f = open(targetFile, 'wb')
pickle.dump(animalList, f)

f.close()

f = open(targetFile, 'rb')
storedFile = pickle.load(f)
print(storedFile)

print("-----------------------")

# 使用文本输出报错: io.UnsupportedOperation: write
f2 = open('04_backup2.txt', 'w', encoding='utf-8')
pickle.dump(animalList, f)

f2.close()

f2 = open('04_backup2.txt', 'r', encoding='utf-8')
storedFile2 = pickle.load(f)
print(storedFile2)

