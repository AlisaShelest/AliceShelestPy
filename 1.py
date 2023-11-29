# print('hello', 'world', sep='---', end='Закончил')
# print('hello', 'world', sep='\n', end=' + ')
# print('hello', 'hello')

# print("Привет. \nЭто кот. Зовут Кокос. Но не тот 'кокос'.")
# Можно в тройные ковычки взять те же самые, но одинкаовые. Либо в ковычки брать другие, одни.

# print('\n')

"""
Многострочный комментарий
"""
# Проверяем id еременных , у еденицы один и тот же id (a = b = c = 1)
# name = 'Vladimir'
# a = 1
# b = 1
# print(id(a))
# print(id(b))
# print(a)

# a, b, = 1, 2 # То же что и a = 1 b = 2
# print(id(b))

# Типы данных ------------
# string = 'Я строка' # Строка все что в ковычках это строка
# integer = 1 # Целое число

# Функция инпут
# data = 'Какие-то данные

# float = 1.0 # Число с плавающей запятой
# string_digit = '1'
# print(type(string))
# print(type(integer))
# print(type(float))
# print(type(int(string_digit)))
# data1 = 'Какие-то данные '
# data = input('Введите число: ')
# print(type(data))

# _name1_a
# name_new = "Elena"
# age = 20
# print("Hello,", name_new)
# print(type(age))
# ctrl slash

# a = b = c = 1
# print(a, b, c)
# a, b, c = "Hello", False, 3.3
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(a)
# print(type(a))
# a = 5
# print(a)
# print(type(a))
# a = 5.5
# print(a)
# print(type(a))
# a = True
# print(a)
# print(type(a))

# name = "Ольга"
# age = 25
# print("Меня зовут " + name + ", мне " + str(age))

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # a, b = b, a  # поменяли значение переменных через множественное присваивание
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка '
# 'символов')

# print("Документ \"file.py\" \t\tнаходится по заданному пути \nD:\\Python\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)  # ctrl d

# print(334566)
# print(-334566)
# print(4)
# print(4.333444555666777999)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 // 2)  # 3
# print(6 ** 2)
# print(7 % 2)

# a, b, c, = 5, 7, 3
# summ = a + b + c
# p = a * b * c
# sa = summ / 3
# print("Сумма:м", summ)
# print("Произведение: ", p)
# print("Среднее арифметическое: ", sa)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num +=5
# print(num)  # 15
# num -= 3
# print(num) # 12
# num *= 4
# print(num)

# words = input("Введите слова: ")
# print(words)

# string = 'Я строка'
# integer = 1
# float = 1.0
# string_digit = '5'
#
# print(type(string))
# print(type(integer))
# print(type(float))
# print(type(int(string_digit)))

# data1 = 10
# data = 'Какие-то данные'
# data = input("Ведите число: ")
# print(data * data1)

# products = ['apple', 'orange', 'pineapple', 'banana', 'mango']
# for product in products:
# print(type(product))
# print(product)

# weekday = 2
# weekend = 5
# total = weekday * 5 + weekend * 2
# print('За неделю я прохожу', total, 'км.')
# side = input('Введите сторону куба: ')
# print('Объем куба равен ', int(side)*int(side)*int(side))

''' salary = input('Сколько вы получаете в месяц? :')
credit = input('Введите ежемесячную сумму платежа по кредиту: ')
service = input('Введите сумму коммунальных платежей за месяц: ')
print('У вас остается',int(salary) - int(credit) - int(service),'т.р.') '''

''' num = int(input('число'))
if num > 0:
    print('положительное')
else:
    print('отрицательное')'''

'''age = int(input('Введите возраст кошки:'))
if age == 0 or age <= 1:
    print('Котеночек')
elif age <= 7:
    print('Взрослая кошка')
elif age > 7 and age <= 99:
    print('Бабка Котунья')
else:
    print('Кошки столько не живут')'''

'''nomer = 1

def talon(bukva):
    print('Ваш талон: ', bukva, nomer)

otvet = input('куда вы хотите? 1 - банк, 2 - цирк, 3 - поликлиника\n')
if otvet == '1':
    talon('Б')
    nomer += 1
elif otvet == '2':
    talon('Ц')
    nomer += 1
elif otvet == '3':
    talon('П')
    nomer += 1'''
'''n = 10
for i in range(10):
    n += 2.5
    print(n)

a = 10
while a < 150:
    a += 2.5
    print(a)'''

'''animals_list = ['cat', 'dog', 'bird', 'koala', 'hamster', 'python', 'mouse']
for a in animals_list:
    print(a, 'sleeps')'''
import random

# n = random.randint(1, 25)
# print(n)

''' croc = 0
while True:
    croc = random.randint(1, 25)
    print(croc)
    if croc >= 25:
        break'''

''' def kubik():
    a = random.randint(1, 6)
    print('   *************')
    print('************   *')
    print('*          *   *')
    print('*  ', (a),'*   *')
    print('*          *   *')
    print('************')'''

'''x = int(input('Ведите число:'))
for i in range(x):
    k = random.randint(1, 100)
    print(k)
    if k%2==0:
        c += k
    a = 0
    b = 0'''

'''a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))
summa = a + b + c
p = a*b*c
d = int(input('Выберите действие: 1 = сумма, 2 = произведение'))
if d == 1:
    print(summa)
elif d == 2:
    print(p)'''

''' a = input('Какое действие вы хотите произвести? + - * /:')
c = int(input('Выберите первое число:'))
d = int(input('Выберите второе число:'))
if a == '+':
    print(c + d)
elif a == '-':
    print(c - d)
elif a == '*':
    print(c * d)
elif a == '/':
    print(c / d)
else:
    print('Неверно выбрано действие')'''

''' def plus():
    print(c + d)
def minus():
    print(c - d)
def multiply():
    print(c * d)
def divide():
    print(c / d)

a = input('Выберите действие + - * /:')
c = int(input('Выберите первое число:'))
d = int(input('Выберите второе число:'))
if a == '+':
    plus()
elif a == '-':
    minus()
elif a == '*':
    multiply()
elif a == '/':
    divide()
else:
    print('Неверно выбрано действие')'''

'''autos = ['BMW', 'Chevrolet', 'Citroen']
def ajust():
    (autos.append(b))
def supprime():
    (autos.remove(c))
a = input('1 - добавить авто, 2 - удалить авто')
if a == '1':
    ajust()
elif a == '2':
    supprime()
else:
    print('Неверное значение')
print(autos)'''

'''autos = ['tesla','chevrolet', 'bmw']
ajust = input('Какой автомобиль хотите добавить?:')
autos.append(ajust)
supprim = input('Какой автомобиль хотите удалить?:')
autos.remove(supprim)
print(autos)'''

'''autos = ['tesla','chevrolet', 'bmw']
ajust = int(input('1 - добавить авто, 2 - удалить авто'))
def f1():
    add = input('Что добавить?:')
    autos.append(add)
    print(autos)
def f2():
    rem = input('Что удалить?:')
    autos.remove(rem)
    print(autos)
if ajust == 1:
    f1()
elif ajust == 2:
    f2()
else:
    print('Неверное значение')'''

'''import random
while True:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sum = a + b
    print('Первый бросил:',a, b)
    if a == b:
        break
while True:
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    sum1 = d + c
    print('Второй бросил:', c, d)
    if c == d:
        break
if sum > sum1:
    print('Первый игрок выйграл')
elif sum < sum1:
    print('Второй игрок выйграл')
else:
    print('Ничья')'''

'''for i in range(1, 11):
    for j in range(1, 11):
        strtable = i * j
        print(f'{j} * {i} = {strtable}\t', end='')
    print('')'''
'''import random
films = ['']

def listen():
    com = input('Скажите команду:')
    vibor(com)
    pass

def vibor(msg):
    msg = msg.lowr()
    if 'привет' in msg:
        action('Привет!')
    elif 'пока' in msg:
        r = random.choice(films)
        action('До свидания')
    elif 'фильм' in msg:
        action('ff')
    else:
        action(msg)
        pass
def action(say):
    print('Бот:',say)
    pass

def action():

    while True:
        listen()'''

'''numer = int(input('Число - начало диапазона\t'))
numer1 = int(input('Число - конец диапазона\t'))

for i in range(numer, numer1+1):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    else:
        print(i)'''

'''num1 = int(input('Введите начало диапазона'))
num2 = int(input('Ввнедите конец диапазона'))
numeros = [i for i in range(num1, num2+1)]

eqv = 0
noneqv = 0

for i in numeros:
    if i % 2 == 0:
        noneqv += i
    elif i % 2 != 0:
        eqv += i
print('Четные сумма:', eqv)
print('Нечетные сумма', noneqv)'''

students = ['Smirnov', 'Ivanov', 'Petrov']
'''def adjust():
    add = input('Какого студента хотите добавить?:')
    students.append(add)
    print(students)
def supprim():
    sup = input('Какого студента хотите удалить?:(Фамилия)')
    try:
        students.remove(sup)
        print(students)
    except:
        print('Такого студента нет')
def numer():
    ind = input('Узнать номер студента:')
    try:
        a = students.index(ind)
        print(a)
    except:
        print('Такого студента нет')
adjust()
supprim()
numer()'''







