import string

str = 'abcdefg'
s2 = str[1:5:2]
s3 = str[::-1]


# print(s2)
# print(s3)


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


list = [' ', ',', '.']
something2 = input("please input something: ")
lowercase = something2.lower()
for item in list:
    lowercase = lowercase.replace(item, '')
print(lowercase)
if is_palindrome(lowercase):
    print("yes, this is a palindrome")
else:
    print("no, this is not palindrome")

print("-------------------")

myList = ['dog', 'cat', 'elegant', 'python']
myList2 = [i[::-1] for i in myList if len(i) > 3]
print(myList2)
