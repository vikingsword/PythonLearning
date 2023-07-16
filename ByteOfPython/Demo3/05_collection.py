# It's similar to the set structure in java
country = set(['China', 'Japan', 'America'])


def fun1():
    if 'Japan' in country:
        # return can't be written in single if statement.
        return True
    elif 'India' in country:
        return False
    else:
        print("country")


res = fun1()
print(res)

countryClone = country.copy()
countryClone.add("India")


def fun2():
    if country.issubset(countryClone):
        return True
    else:
        return False


print(fun2())

print(country & countryClone)

countryClone.remove("India")
print(country == countryClone)
