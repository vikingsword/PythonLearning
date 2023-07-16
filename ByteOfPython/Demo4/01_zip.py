import os
import time

source = ['E:\\Sec\\Language\\Python\\Project\\Mess\\byteofpython\\Demo4\\01_sourcefile.txt']
#
source2 = ['E:\\Sec\\Language\\Python\\Project\Mess\\byteofpython\\Demo4\\01_sourcefile.txt']
# 如果是当前目录就直接写文件名就行！！！
source3 = ['01_sourcefile.txt']
target_dir = 'E:\\Sec\\Language\\Python\\Project\\Mess\\byteofpython\\Demo5'
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

print('os.getcwd = ', os.getcwd())
print('os.sep = ', os.sep)
print("target = ", target)
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# sourceFile = os.getcwd() + os.sep + source3[0]
sourceFile = source3[0]
zip_command = 'zip -r {0} {1}'.format(target, sourceFile)
print('Zip	command	is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful	backup	to', target)
else:
    print('Backup failed')
