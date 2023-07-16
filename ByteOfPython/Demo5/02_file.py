import io

poem = '''\
Programming	is	fun
When	the	work	is	done
if	you	wanna	make	your	work	also	fun:
use	Python!
'''
f = open("poem.txt", 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    r = f.readline()
    if len(r) == 0:
        break
    print(r, end='')
f.close()

# help(open())

print("-------------------------")

f = io.open('02_poem.txt', 'wt', encoding='utf-8')
f.write(poem)
f.close()

f = io.open('02_poem.txt', 'rt', encoding='utf-8')
# 如果不循环读取,只会读取到第一行
r = f.readline()
print(r)
f.close()

with open('02.txt', 'a', encoding='utf-8') as f:
    f.write('xxx')
    f.close()
