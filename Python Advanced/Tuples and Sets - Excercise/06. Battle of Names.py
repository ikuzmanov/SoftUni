count_of_names = int(input())

odd_set = set()
even_set = set()
name_collection = 0

for row in range(1, count_of_names + 1):
    name = input()
    for char in name:
        char = int(ord(char))
        name_collection += char
    name_collection = int(name_collection / row)
    if name_collection % 2 == 0:
        even_set.add(name_collection)
    else:
        odd_set.add(name_collection)

    name_collection = 0

sum_of_even_sets = sum(even_set)
sum_of_odd_sets = sum(odd_set)

if sum_of_odd_sets == sum_of_even_sets:
    print(*odd_set.union(even_set), sep=", ")

elif sum_of_odd_sets > sum_of_even_sets:
    print(*odd_set.difference(even_set), sep=", ")

elif sum_of_even_sets > sum_of_odd_sets:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
