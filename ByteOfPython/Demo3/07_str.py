name = "Vikingar"

if name.startswith("vik"):
    print("yes1")

if name.startswith("Vik"):
    print("yes4")

if name.endswith("ar"):
    print("yes2")

if name.find("king"):
    print(name.find("king"))

delimiter = "_"
print(name.join(delimiter))

mylist = ['zs', 'ls', 'ls']
print(delimiter.join(mylist))
