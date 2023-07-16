# 自定义异常，需要继承基类Exception
class MyException(Exception):
    def __init__(self, content):
        Exception.__init__(self)
        self.content = content


filterList = ['<', '>', 'script', 'alert']

try:
    text = input("please input you payload: ")
    for item in filterList:
        if text.find(item):
            raise MyException(text)
except EOFError:
    print('why did you do EOF on me ?')
except MyException as ex:
    print('you input content: \'{0}\' include forbid character: \'{1}\''.format(text, item))
else:
    print('you input successful')
