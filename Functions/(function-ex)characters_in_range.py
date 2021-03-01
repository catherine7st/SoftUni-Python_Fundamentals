def characters(str1, str2):
    if ord(str1) < ord(str2):
        for el in range(ord(str1) + 1, ord(str2)):
            print(chr(el), end=" ")
    else:
        for el in range(ord(str2) + 1, ord(str1)):
            print(chr(el), end=" ")

    return


string1 = input()
string2 = input()

characters(string1, string2)
