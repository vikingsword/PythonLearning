with open('05_backup.txt') as f:
    for line in f:
        print(line, end='')
    print("\n------------")

with open('04_backup.txt', encoding='utf-8') as f2:
    for text in f2:
        print(text, end='')
    print("\n----------")

with open('05_backup.txt') as f3:
    for line in f3:
        print(line, end='')
