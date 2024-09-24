import time

list = [1, 5, 6, 3, 76, 83, 3, 6, 7, 3, 0]

start = time.time()


def sort_bubble(list):
    is_change = True

    while is_change:
        is_change = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_change = True


sort_bubble(list)
stop = time.time()

# print(list, stop-start)


start = time.time()
list = [1, 5, 6, 3, 76, 83, 3, 6, 7, 3, 0]


def sort_bubble_2(list):
    max_index = len(list) - 1
    for i in range(max_index, 0, -1):
        is_change = False
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_change = True
        if not is_change:
            break


sort_bubble_2(list)
stop = time.time()

# print(list, stop-start)


print("-" * 15, "LAB", "-" * 15)

import random

list_1 = [random.randint(0, 10000) for x in range(10000)]
list_2 = list_1.copy()
list_3 = list_1.copy()

def xd(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



start = time.time()
xd(list_3)
stop = time.time()


def bubble_sort_not_optimalized(arr):
    is_change = True

    while is_change:
        is_change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_change = True


start = time.time()
bubble_sort_not_optimalized(list_1)
stop = time.time()



def bubble_sort_optimalized(arr):
    max_index = len(arr) - 1

    for i in range(max_index, 0, -1):
        is_change = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_change = True

        if not is_change:
            break

start = time.time()
bubble_sort_optimalized(list_2)
stop = time.time()



import timeit

print(timeit.timeit("xd(list_3.copy())", globals=globals(), number=1))
print(timeit.timeit("bubble_sort_not_optimalized(list_1.copy())", globals=globals(), number=1))
print(timeit.timeit("bubble_sort_optimalized(list_2.copy())", globals=globals(), number=1))

