# 这里使用 open 方法也可以正常执行(没有用io模块)
# 即使使用了gbk编码也能将utf-8正常解析

targetFileName = '06_backup.txt'
f = open(targetFileName, 'w', encoding='utf-8')
f.write("hello this is vikingar, nice to meet you!")
f.close()

f = open(targetFileName, 'r', encoding='gbk')
text = f.read()
print(text)
