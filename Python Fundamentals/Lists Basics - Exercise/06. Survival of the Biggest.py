start_list = input()
numbers_to_remove = int(input())

# converting the list to int
list_of_integer = list(map(int, start_list.split()))

#iterating through the list
for number in range(numbers_to_remove):
    list_of_integer.remove(min(list_of_integer))
string_list = ", ".join(map(str, list_of_integer))
print(string_list)