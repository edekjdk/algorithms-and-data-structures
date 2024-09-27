def insert_sorting(list):
    for border in range(1, len(list)):
        current_index = border - 1
        value = current_index + 1

        while list[current_index] > value and current_index >= 0:
            list[current_index+1] = list[current_index]
            current_index -= 1
        list[current_index+1] = value


list = [1,2,34,1,11,1,1]

insert_sorting(list)

print(list)




def insert_sorting_2(list):
    for border in (1,len(list)):
        curr_index = border - 1
        value = curr_index + 1

        while list[curr_index] > value and list[curr_index] >= 0:
            list[curr_index+1] = list[curr_index]
            curr_index -= 1
        list[curr_index+1] = value