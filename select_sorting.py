list = [1, 3, 9, 2, 0, 6, 4, 7, 5, 3]


def select_sort(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run+1, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]

select_sort(list)

print(list)




def select_sorting_2(list):
    for run in range(len(list)):
        min_index = run
        for i in range(run, len(list)):
            if list[i] < list[min_index]:
                min_index = i
        list[run], list[min_index] = list[min_index], list[run]