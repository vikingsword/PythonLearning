# 备份数量过多时，以当天日期为文件夹名，并为文件名加上用户注释
import os
import time

fileName = ['01_sourcefile.txt']
sourceFile = os.getcwd() + os.sep + ' '.join(fileName)

target = ['E:\\Sec\\Language\\Python\\Project\\Mess\\byteofpython\\Demo5']
today = time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

targetDir = target[0] + os.sep + today
print("targetDir = ", targetDir)

if not os.path.exists(targetDir):
    os.mkdir(targetDir)

command = input("please input your command: ")
if len(command) == 0:
    targetFile = targetDir + os.sep + today + '_' + now + '.zip'
else:
    targetFile = targetDir + os.sep + today + '_' + now + '_' + command.replace(' ', '_') + '.zip'
print('targetFile = ', targetFile)

zip_command = 'zip -r {0} {1}'.format(targetFile, sourceFile)

print("zip Command is :", zip_command)
print("Running...")
if os.system(zip_command) == 0:
    print('Successful！')
else:
    print('Filed')
