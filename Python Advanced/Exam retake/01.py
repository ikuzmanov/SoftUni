from collections import deque

ramen_bowls = [int(num) for num in input().split(", ")]
customers = deque([int(num) for num in input().split(", ")])

while True:
    if not customers or not ramen_bowls:
        break
    first_customer = customers[0]
    last_ramen_bowl = ramen_bowls[-1]

    if last_ramen_bowl > first_customer:
        ramen_bowls[-1] -= customers[0]
        customers.popleft()

    elif first_customer > last_ramen_bowl:
        customers[0] -= ramen_bowls[-1]
        ramen_bowls.pop()

    else:
        ramen_bowls.pop()
        customers.popleft()

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join([str(bowl) for bowl in ramen_bowls])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(cust) for cust in customers])}")
