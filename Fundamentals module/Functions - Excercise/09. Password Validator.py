from string import ascii_letters, digits


def is_valid(is_valid_password):
    pass_as_letter = []
    text = []
    digit = 0
    letters = 0
    for symbol in is_valid_password:
        pass_as_letter.append(symbol)
    for i in pass_as_letter:
        if i.isdigit() == True:
            digit += 1
    for letter in pass_as_letter:
        if letter.isalpha() == True:
            letters += 1
    if digit > 1 and letters == len(is_valid_password) - digit and 6 <= len(is_valid_password) <= 10:
        text.append('Password is valid')
    if len(is_valid_password) > 10 or len(is_valid_password) < 6:
        text.append('Password must be between 6 and 10 characters')
    if set(is_valid_password).difference(ascii_letters + digits):
        text.append('Password must consist only of letters and digits')
    if digit < 2:
        text.append('Password must have at least 2 digits')
    return text


password = input()
result = is_valid(password)
print('\n'.join(result))