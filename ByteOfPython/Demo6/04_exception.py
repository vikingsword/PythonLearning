import io
import sys
import time

targetFileName = '04_backup.txt'
try:
    f = io.open(targetFileName, 'w', encoding='utf-8')
    f.write('hello my name is vikingar! nice to meet you！')

    time.sleep(1)

    f = io.open(targetFileName, 'r', encoding='utf-8')
    while True:
        text = f.readline()
        if len(text) == 0:
            break
        print(text, end='')
        sys.stdout.flush()
        # 命令行里按 ctrl+c,pycharm中直接按红色小方块停止程序就行了
        print('Press ctl+c now ')
        time.sleep(3)
except IOError:
    print('could not find file to open')
except KeyboardInterrupt:
    print('You cancelled the reading from the file')
finally:
    if f:
        f.close()
        print('Cleaning up: Closed the file!')

