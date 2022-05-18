divisor = int(input())
max_num = int(input())

for i in range(max_num, divisor - 1, -1):
    if i % divisor == 0:
        print(i)
        break