def palindrome(string):
    for each_str in string:
        if each_str == each_str[::-1]:
            print('True')
        else:
            print('False')
    return string


current_string = input().split(", ")
palindrome(current_string)