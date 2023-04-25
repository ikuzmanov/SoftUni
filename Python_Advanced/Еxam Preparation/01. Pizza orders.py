from collections import deque

def process_pizzas(pizzas, employees):
    total_pizza_count = 0
    while pizzas and employees:
        while pizzas[0] > employees[-1]:
            total_pizza_count += employees[-1]
            pizzas[0] = pizzas[0] - employees[-1]
            employees.pop()

            if not pizzas or not employees:
                return total_pizza_count

        total_pizza_count += pizzas.popleft()
        employees.pop()
    return total_pizza_count


pizzas = deque([int(num) for num in input().split(", ") if 0 < int(num) < 11])
employees = [int(num) for num in input().split(", ")]

total_pizza_count = process_pizzas(pizzas, employees)

if pizzas:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizzas])}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_count}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")