number_input = input().split(", ")


def palindrome(num_list):
    is_it_palindrome = []
    for num in num_list:
        if num == num[::-1]:
            is_it_palindrome.append("True")
        else:
            is_it_palindrome.append("False")

    return is_it_palindrome


result = palindrome(number_input)
print("\n".join(result))
