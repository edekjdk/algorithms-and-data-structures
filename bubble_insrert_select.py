import random
import timeit

list = [random.randint(1, 1000) for i in range(1000)]
list2 = list.copy()
list3 = list.copy()

print(list)

# print(random.randint(1, 1000) for i in range(100))


def bubble(list):
    max_index = len(list)-1
    for i in range(max_index, 0, -1):
        is_changing = False
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                is_changing = True
        if not is_changing:
            break

bubble(list)
print(list)


def insert(list):
    for sort_border in range(1,len(list)):
        curr_index = sort_border - 1
        value = list[curr_index + 1]

        while list[curr_index] > value and curr_index >= 0:
            list[curr_index+1] = list[curr_index]
            curr_index -= 1
        list[curr_index + 1] = value

print("-" *  40)
print(list2)
insert(list2)
print(list2)

print("-" *  40)
print(list3)

def select(list):
    for run in range(len(list)):
        min_index = run
        for i in  range(run + 1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]

select(list3)
print(list3)

print(timeit.timeit("bubble(list)", globals=globals(), number=1))
print(timeit.timeit("insert(list2)", globals=globals(), number=1))
print(timeit.timeit("select(list3)", globals=globals(), number=1))
