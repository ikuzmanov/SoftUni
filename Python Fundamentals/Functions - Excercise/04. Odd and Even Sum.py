number_input = input()

def odd_or_even(number):

    odd_sum = 0
    even_sum = 0

    for num in number:
        num = int(num)
        if num % 2 == 0:
            even_sum += num
        elif num % 2 != 0:
            odd_sum += num

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

odd_or_even(number_input)