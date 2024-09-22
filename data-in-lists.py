my_numbers = list(range(10))
print(my_numbers)

squared_Numbers = [x * x for x in my_numbers]
squared_Numbers2 = [(lambda x: x * x)(x) for x in my_numbers]

print(squared_Numbers)
print(squared_Numbers2)


names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']

def get_sub_name(name, part):
    parted = name.split()
    if part == 1:
        return parted[1]
    else:
        return parted[0]

# only_names_1 = []
# for i in names:
#     only_names_1.append(get_sub_name(i, 0))
#
# only_last_names_1 = []
# for i in names:
#     only_last_names_1.append(get_sub_name(i, 1))
#
# print(only_names_1)
# print(only_last_names_1)

only_names_1 = [get_sub_name(name,0) for name in names]
only_last_names_1 = [get_sub_name(name,1) for name in names]
print(only_names_1)
print(only_last_names_1)


only_names_2 = [(lambda name: name.split()[0])(name) for name in names]
only_last_names_2 = [(lambda name: name.split()[1])(name) for name in names]

print(only_names_2)
print(only_last_names_2)

only_names_3 = [name.split()[0] for name in names]
only_last_names_3 = [name.split()[1] for name in names]

print(only_names_3)
print(only_last_names_3)



