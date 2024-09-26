import random
import timeit

list_1 = [random.randint(0, 10000) for x in range(10000)]
list_2 = list_1.copy()
list_3 = list_1.copy()


def insert_sorting(list):
    for sort_border in range(1, len(list)):
        curr_index = sort_border - 1
        value = list[curr_index + 1]


        while list[curr_index] > value and curr_index >= 0:
            list[curr_index + 1] = list[curr_index]
            curr_index = curr_index - 1
        list[curr_index + 1] = value


def bubble_sort(list):
    max_index = len(list) - 1
    for i in range(max_index, 0, -1):
        is_changing = False
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_changing = True
        if not is_changing:
            break



print(timeit.timeit("insert_sorting(list_1)", globals=globals(), number=1))
print(timeit.timeit("bubble_sort(list_2)", globals=globals(), number=1))
print(timeit.timeit("sorted(list_3)", globals=globals(), number=1))


def inster_sort_2(list):
    for sort_border in range(1, len(list)):
        current_index = sort_border - 1
        value = list[current_index + 1]

        while list[current_index] > value and current_index >= 0:
            list[current_index+1] = list[current_index]
            current_index -= 1
        list[current_index+1] = value