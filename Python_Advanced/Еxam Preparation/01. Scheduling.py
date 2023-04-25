from collections import deque

clock_cycles = deque([int(num) for num in input().split(", ")])
job_index = int(input())

job = clock_cycles[job_index]

print(sum([num for num in clock_cycles if num <= job]))
