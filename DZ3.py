## 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9


def print_crat_num():
    for i in range(2,10):
         print (f'чисел кратных {i} : {99 // i}')

##2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def num_min_max(arr: list):
    min_id = 0
    max_id = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_id]:
            min_id = i
        elif arr[i] > arr[max_id]:
            max_id = i
    print(arr[min_id], arr[max_id])





#3 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

def num_sum_range_min_max(arr: list):
    min_id = 0
    max_id = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_id]:
            min_id = i
        elif arr[i] > arr[max_id]:
            max_id = i
    if min_id > max_id:
        min_id, max_id = max_id, min_id
    summa = 0
    for i in range(min_id+1, max_id):
        summa += arr[i]
    print(summa)



#4

def search_2min(array: list):
    min1 = min(array)
    array.remove(min1)
    min2 = min(array)
    print(min1, min2)


print("-----------1 задание--------------")
print_crat_num()
print("-----------2 задание---------------")
num_min_max([22,2,33,1,11,77,95])
print("-----------3 задание---------------")
num_sum_range_min_max([1,22,2,33,1,11,77,95])
print("-----------4 задание---------------")
search_2min([2,22,2,33,3,11,77,1,95])