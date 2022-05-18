num_1 = int(input())
num_2 = int(input())

my_list = []
for num in range(num_1, num_1*num_2+1):
    if num % num_1 == 0:
        my_list.append(num)

print(my_list)