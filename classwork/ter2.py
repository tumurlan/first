names = ['JACK', 'JIMMY', 'JACKSON', 'JACKSON', 'JHON', 'JACKSON', 'JHON', 'JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON', 'JACKSON', 'JHON', 'JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
r = 0
while r < 5:
    if r % 2 ==0:
       names.pop(r)
    if r % 2 ==1:
       names.pop(r)
    r += 1
print(names) 
