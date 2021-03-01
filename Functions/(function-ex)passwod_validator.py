def password_validator(word):
    is_valid = True
    if not 6 <= len(word) <= 10:
        is_valid = False
        print('Password must be between 6 and 10 characters')

    is_not_digit = False

    digits = 0
    for character in word:
        if not character.isdigit() and not character.isalpha():
            is_valid = False
            print('Password must consist only of letters and digits')
            break

        if character.isdigit():
            digits += 1
    if digits < 2:
        is_valid = False
        print('Password must have at least 2 digits')

    return is_valid


password = input()
is_valid = password_validator(password)

if is_valid:
    print('Password is valid')
