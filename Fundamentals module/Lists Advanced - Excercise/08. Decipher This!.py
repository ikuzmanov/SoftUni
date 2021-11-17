secret_message = input().split()
for char in secret_message:
    char = list(char)
    first_later = ""
    for number in char:
        if number.isdigit():
            first_later = first_later + number
        else:
            break
    first_letter_to_add = chr(int(first_later))
    char.insert(0, first_letter_to_add)
    char =''.join([i for i in char if not i.isdigit()])
    char = list(char)
    char[1], char[-1] = char[-1], char[1]
    print(''.join(char), end=' ')