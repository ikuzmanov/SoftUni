count_of_inputs = int(input())
queries_stack = []

for _ in range(count_of_inputs):
    query = input().split()
    command = query[0]
    if command == "1":
        number = int(query[1])
        queries_stack.append(number)
    elif command == "2" and queries_stack:
        queries_stack.pop()
    elif command == "3" and queries_stack:
        print(max(queries_stack))
    elif command == "4" and queries_stack:
        print(min(queries_stack))

queries_stack.reverse()
print(*queries_stack, sep=", ")
