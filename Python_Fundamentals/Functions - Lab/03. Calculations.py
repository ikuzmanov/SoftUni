operator = input()
first_num = int(input())
second_num = int(input())

def calculate(operator:str, first_num:int, second_num:int):

    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return first_num / second_num
    elif operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num
    else:
        print("Wrong operator.")

print(calculate(operator, first_num, second_num))