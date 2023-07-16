import io

targetFileName = '05_backup.txt'
f = io.open(targetFileName, 'w', encoding='utf-8')
f.write("hello this is my output file")
f.close()

text = io.open(targetFileName, encoding='utf-8').read()
print(text)
