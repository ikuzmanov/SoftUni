from collections import deque as dq

n_pumps = int(input())
pumps = dq()

for i in range(n_pumps):
    pumps.append([int(i) for i in input().split()])

index = 0
tank_full = 0
to_be_filled = []

while pumps:
    amount, distance = pumps.popleft()
    to_be_filled.append([amount, distance])
    if tank_full + amount >= distance:
        tank_full = tank_full + amount - distance
    else:
        pumps.extend(to_be_filled)
        index += len(to_be_filled)
        to_be_filled = []
        tank_full = 0

print(index)