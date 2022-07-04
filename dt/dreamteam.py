'''
#1
num = 1
sum = 0

while num < 1000:
    num += 1
    if num%3 == 0 or num%5 == 0:
        sum += num
print(sum)

#2
a = 333
b = 555
c = 0
c = a
a = b
b = c
print(a)#555
print(b)#333


#3
numbers = input('Vvedite chisla: ')
sum = sum(map(int, numbers.split()))
print(sum)
'''
#4
date = {"year": "2020","month": "10", "day": "24", "time": "18:30"}
a = input('Введите дату в формате YYYY-MM-DD TIME: ')
year = a[:4]
month = a[5:7]
day = a[8:10]
time = a[11:]
date.update({'year':year})
date['month']=month
date['day']=day
date['time']=time
print(date)
'''
#6
sent = ' '
numwords = 5
for i in range(1, numwords + 1):
    word = input('Enter: ')
    sent = sent + word + ' '
print(numwords)

#(2)1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for b in a:
    if b > 5:
        print(b)

#(2)3
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
lst = list(spisok_2)
lst1  = list(spisok_1)
print(type(lst))
result = list(set(spisok_2) - set(spisok_1))
print(result)

#(3)1
x = 1
while x <= 300:
    x += 1
    if  x%2 == 0 or x == 237:
        print(x)
#(3)2
name = input('Введите имя пользователя: ')
a = name.split(' ')
c = len(a)
b = True

while True:
        if c>=6:
                break
        else:
                name = input('Введите имя пользователя: ')

if a%2 == 0:
        q = a[:len(a)//2]
        w = a[len(a)//2:]
else :
        q = a[:(len(a)//2)+1]
        w = a[(len(a)//2)+1:]
q,w = w,q
print(q+w)

#(3)3
numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]

numbers.remove(-3.3)
numbers.remove(7.1)
numbers.remove(8.4)
print(numbers)

even, odd = 0, 0

for n in numbers:
    if n%2 == 0:
        even += 1
    if n%2 != 0:
        odd += 1

print(even, odd)

#(3)5
my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
for num in my_list:
    if num % 2 == 0:
        print(num, end =' ')

#1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Выберите знак.")
print("1.Плюс")
print("2.Минус")
print("3.Умножение")
print("4.Деление")

while True:
    choice = input("Выберите (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Еще раз воспользуетесь калькулятором? (да/нет): ")
        if next_calculation == "нет":
            break
     else:
         print("Введите цифру: )
'''
