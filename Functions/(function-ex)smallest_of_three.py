def smallest_of_three(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num1 > num3 and num3 < num2:
        return num3


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(smallest_of_three(number1, number2, number3))

