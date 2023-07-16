def get_error_detail():
    return (2, 'detail')


errnum, errstr = get_error_detail()
print(errnum)
print(errstr)

print("------------------")

a, b = 1, 2
a, b = b, a
print(a)
print(b)

