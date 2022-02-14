## 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sumAndMult():
    sum = 0
    mult = 1
    inputnum = int(input('трехзначное целое число'))
    if ((99 < inputnum) and (inputnum <1000)):
        list = [int(a) for a in str(inputnum)]
        for item in list:
            sum = sum + item
            mult = mult * item
        print("Сумма %.0f произведение %.0f" %( sum, mult))
    else:
        print("Введено не корректное число. Число должно быть целым, трехзначным!")

## 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

def bitOperation():
    num1 = 5
    num2 = 6
    print("Побитовое И над числами  %.0f и %.0f равно %.0f" %( num1, num2, (num1 & num2)))
    print("Побитовое ИЛИ над числами  %.0f и %.0f равно %.0f" %( num1, num2, (num1 | num2)))
    print("Побитовое исключающееИЛИ над числами  %.0f и %.0f равно %.0f" % (num1, num2, (num1 ^ num2)))
    print("Побитовое двоной битовый сдвиг лево над числом  %.0f равно %.0f" % (num1, (num1<<2)))
    print("Побитовое двоной битовый сдвиг вправо над числом  %.0f равно %.0f" % (num1, (num1>>2)))

## 3.По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

def funcEquation():
    x1, y1, x2, y2 = [ int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split() ]
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print('Уравнение прямой для введенных координат: y = %fx + %f'%(k , b))

## 4. Написать программу, которая генерирует в указанных пользователем границах:
## случайное целое число;
## случайное вещественное число;
## случайный символ.
## Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import randint

def listAbc(chr1, chr2):
    return  [chr(i) for i in range(ord(chr1), ord(chr2) + 1, 1)]


def frange(start, stop, jump):
    while start < stop:
        yield start
        start += jump

def randomItemRange():
    type = int(input("Введите: 1 если целое число \n 2 если вещественное число\n 3 если символ"))
    if type == 1 :
        range1, range2 = [int(x) for x in input('Введите границы для вывода случайного числа через запятую ): ').split(",")]
        if range1 < range2:
            print(randint(range1,range2))
        else:
            print('Водите целые числа в диапазоне от меньшего числа к большему')

    elif type == 2 :
        startfloat, stopfloat = [float(x) for x in
                          input('Введите границы для вывода случайного символа через запятую ): ').split(",")]
        list_float = [x for x in frange(startfloat, stopfloat + 1, 1)]
        floatrand = list_float[randint(1, len(list_float))]
        print(f'Случайнове вещественное число из диапазона {startfloat} - {stopfloat}: {floatrand}')

    elif type == 3 :
        startchr, stopchr = [x for x in
                          input('Введите границы для вывода случайного символа через запятую ): ').split(",")]
        list_abc = listAbc(startchr, stopchr)
        print(list_abc)
        chrrand= list_abc[randint(1, len(list_abc))]
        print(f'Случайный символ из диапазона {startchr} - {stopchr}: {chrrand}')

    else:
        print('Такого выбора нет')
## 5 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def simvolSearch(simlist, simvol):
    for i in range (len(simlist)):
        if simlist[i] == simvol:
            return i
    return -1

def simvol_abc():
    list_abs = listAbc("a","z")
    chr1 = input('Введите первый символ: ')
    chr2 = input('Введите второй символ: ')
    indexChr1 = simvolSearch(list_abs,chr1.lower())
    indexChr2 = simvolSearch(list_abs,chr2.lower())
    print(list_abs)
    print(f'Cимвол {chr1.lower()} находиться на  {indexChr1 + 1}')
    print(f'Cимвол {chr2.lower()} находиться на  {indexChr2 + 1}')
    print(f'Между символами  {chr1.lower()} и {chr2.lower()} находится {abs(indexChr2 - indexChr1) - 1} символа.')

## 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def serachSimvol():
    list_abs = listAbc("A","Z")
    print(list_abs)
    numSimvol = int(input('Введите номер символа в алфавите от 1 до 27: '))
    print(f'Под номеров {numSimvol} в алфавите находется буква {list_abs[numSimvol - 1]}')

## 7.По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
def isTriangle():
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    c = int(input("Введите сторону c = "))
    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует")
    elif a != b and a != c and b != c:
        print("Разносторонний")
    elif a == b == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")

## 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def isLeapYear(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

## 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def avgNum():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))

    if b < a < c or c < a < b:
        print('Среднее:', a)
    elif a < b < c or c < b < a:
        print('Среднее:', b)
    else:
        print('Среднее:', c)

## Свич для запуска отдельных заданий

while(True):
    i = int(input('Введите номер задане  от 1 до 9 или любо другой символ для выхода: '))
    if i == 1:
        sumAndMult()
    elif i == 2:
        bitOperation()
    elif i == 3:
        funcEquation()
    elif i == 4:
        randomItemRange()
    elif i == 5:
        simvol_abc()
    elif i == 6:
        serachSimvol()
    elif i == 7:
        isTriangle()
    elif i == 8:
        print(isLeapYear(int(input("Введите год\n"))))
    elif i == 9:
        avgNum()
    else:
        break

