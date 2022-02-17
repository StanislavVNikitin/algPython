## 1. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def costEvenAndOddNum():
    num = input('Введите натуральное число: ')
    counte = 0
    counto = 0
    if int(num):
        listNum =list(num)
        for item in listNum:
            if int(item)%2:
                counto +=1
            else:
                counte +=1

    print(f"в числе {num} четных чисел {counte} нечетных чисел {counto}")

## 2 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)
def revsNumStr(num):
    return int(str(num)[::-1])

def revsNum(num):
    orignum = num
    revsNumber = 0
    while (num > 0):
        remainder = num % 10
        revsNumber = (revsNumber * 10) + remainder
        num = num // 10

    return f"Переданное число: {orignum} перевернутое число: {revsNumber}"

## 3. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def sumNItemRange(n: int):
    item = 1
    sumItemRange = 0
    for i in range(n):
        sumItemRange += item
        item /= -2

    return sumItemRange

## 4. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
def equalityCheck(n:int):
    sumNum = 0
    for i in range(1,n+1):
        sumNum += + i

    return sumNum == (n * (n+1)/2)

## 5. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
def countingNum():
    countInputNum = int(input("Количество  вводимых чисел"))
    searchNum = int(input("Введите искомое число"))
    count = 0
    n = 1
    while(n < countInputNum+1):
        itemNum = int(input("Введите число № " + str(n) + ": "))
        n+=1
        while itemNum > 0:
            if ((itemNum % 10) == searchNum):
                count +=1
            itemNum = itemNum // 10
    
    return f"Введенных числах  цифр {searchNum} встречается {count} раз"

## 6. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр. Дополнительно (рекурсивно)
def rec_max_sum():
    def sumNum(num: int):
        num = int(num)
        if (num/10 != 0):
            return num%10 + sumNum(int(num/10))
        else:
            return num%10

    countInputNum = int(input("Количество  вводимых чисел"))
    sumNumMax = 0
    sumNumMaxNum = 0
    n=1
    while (n < countInputNum + 1):
        itemNum = int(input("Введите число № " + str(n) + ": "))
        print(sumNum(itemNum))
        if (sumNumMax == 0) or (sumNumMax < sumNum(itemNum)):
            stepNum = n
            sumNumMax = sumNum(itemNum)
            sumNumMaxNum = itemNum
        n += 1

    return f"Число: {sumNumMaxNum} с максимальной суммой чисел: {sumNumMax} было введено на {stepNum} шаге"


## Свич для запуска отдельных заданий
while(True):
    i = int(input('Введите номер задане  от 1 до 6 или любо другой символ для выхода: '))
    if i == 1:
        costEvenAndOddNum()
    elif i == 2:
        print(revsNum(56783470100))
    elif i == 3:
        print(sumNItemRange(10))
    elif i == 4:
        print(equalityCheck(85))
    elif i == 5:
        print(countingNum())
    elif i == 6:
        print(rec_max_sum())
    else:
        print("Пока")
        break

