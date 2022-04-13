from collections import deque

customers = deque([int(num) for num in input().split(", ")])
taxis = [int(num) for num in input().split(", ")]

total_time_passed = sum(customers)

while customers and taxis:
    customer_to_take = customers[0]
    taxi_to_take = taxis[-1]
    if taxi_to_take >= customer_to_take:
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time_passed} minutes")

else:
    print(f"Not all customers were driven to their destinations\n" 
          f"Customers left: {', '.join(str(num) for num in customers)}")
