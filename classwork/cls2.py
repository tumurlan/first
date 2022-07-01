a = int(input("cislo1: "))
b = int(input("cislo2: "))
c = int(input("cislo3: "))

if a > b and a > c:
    print(a) 
elif b > a and b > c:
    print(b)
elif c > b or c > a:
    print(c)

