from collections import deque

total_food = int(input())
orders = deque([int(num) for num in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]

    if current_order > total_food:
        break

    total_food -= current_order
    orders.popleft()

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")

