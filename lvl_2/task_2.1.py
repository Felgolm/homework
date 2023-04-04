# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    min_val = None
    for val in arr:
        if min_val is None:
            min_val = val
        if val < min_val:
            min_val = val
    return min_val


def maximum(arr):
    max_val = None
    for val in arr:
        if max_val is None:
            max_val = val
        if val > max_val:
            max_val = val
    return max_val


# Проверка
list_of_lists = [
    [4, 6, 2, 1, 9, 63, -134, 566],  # -> max = 566, min = -134
    [-52, 56, 30, 29, -54, 0, -110],  # -> min = -110, max = 56
    [42, 54, 65, 87, 0],  # -> min = 0, max = 87
    [5]  # -> min = 5, max = 5
]

for list_ in list_of_lists:
    print('Принятый список:', list_)
    print("минимум:", minimum(list_))
    print("максимум:", maximum(list_))
    print('=' * 10 + '\n')

# Можно кстати через быструю сортировку
# Быстрая сортировка
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
