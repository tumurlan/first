print('list')
list = ['']
while len(list) != 5:
    name = input(': ')
    list.append(name)
protect_list = tuple(list)
print(protect_list)

