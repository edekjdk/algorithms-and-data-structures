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

list_1 = [random.randint(0, 100000) for x in range(10000)]
list_2 = list_1.copy()
list_3 = list_1.copy()
list_4 = list_1.copy()
list_5 = list_1.copy()
list_6 = list_1.copy()

def xd(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



start1 = time.time()
# xd(list_4)
stop1 = time.time()


def bubble_sort_not_optimalized(arr):
    is_change = True

    while is_change:
        is_change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_change = True


start2 = time.time()
# bubble_sort_not_optimalized(list_5)
stop2 = time.time()



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

start3 = time.time()
# bubble_sort_optimalized(list_6)
stop3 = time.time()



import timeit

print(timeit.timeit("xd(list_3)", globals=globals(), number=1))
print(timeit.timeit("bubble_sort_not_optimalized(list_1)", globals=globals(), number=1))
print(timeit.timeit("bubble_sort_optimalized(list_2)", globals=globals(), number=1))

