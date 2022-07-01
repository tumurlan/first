list = []

while len(list) != 3:
    name = input(': ')
    dob = input(': ')
    fpl = input(': ')
    list.append(name)
    list.append(dob)
    list.append(fpl)
list1 = tuple(list)
print(list1)
