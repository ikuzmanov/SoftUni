count = int(input())
for i in range(0,count):
    for k in range(0,count):
        for j in range(0,count):
            print(f"{chr(97+i)}{chr(97+k)}{chr(97+j)}")