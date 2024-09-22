from functools import reduce

my_list = [1, 2, 3, 4, 5]
animals = ["cat", "dog", "snake", "elemele", "eme"]

squares = list(map(lambda x: x * x, my_list))
upper_animals1 = list(map(lambda x: x.upper(), animals))
# upper_animals2 = [x.upper() for x in animals]
# upper_animals3 = [(lambda x: x.upper())(x) for x in animals]


print(squares)
print(upper_animals1)
# print(upper_animals2)
# print(upper_animals3)

animals_with_3_letters = list(filter(lambda x: len(x) == 3, animals))
print(animals_with_3_letters)

animals_with_e_ending = list(filter(lambda x: x[-1] == "e", animals))
print(animals_with_e_ending)

list_with_numbers = [12, 14, 2, 1, 10, 19, 33]

sum_of_numbers = reduce(lambda x, y: x + y, list_with_numbers)
max_number = reduce(lambda x, y: x if x > y else y, list_with_numbers)
min_number = reduce(lambda x, y: x if x < y else y, list_with_numbers)

print(sum_of_numbers, sum(list_with_numbers))
print(max_number, max(list_with_numbers))
print(min_number, min(list_with_numbers))

random_data_to_sort = [".23", ".1", ".34", ".2", ".78"]
sorted_data = sorted(random_data_to_sort, key=lambda x: int(x[1:]))

print(sorted_data)

print("-" * 15, "LAB", "-" * 15)

list_to_sort = [1, 45, 672, 7265, 16]

sorted_list_to_sort = sorted(map(str, list_to_sort), key=lambda x: int((x[-1])))

print(sorted_list_to_sort)


codes = ['JPID', 'JJJPPP', 'XXX', 'JDU']

longest = reduce(lambda x,y: x if x > y else y, map(len, codes))
longest2 = reduce(lambda x, y: x if len(x) > len(y) else y, codes)

print(longest)
print(longest2)

capitals =['Rome', 'Paris', 'Madrid']
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']

not_capitals = list(filter(lambda x: x not in capitals, cities))

print(not_capitals)