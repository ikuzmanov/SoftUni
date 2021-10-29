def is_perfect(some_number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if sum == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))