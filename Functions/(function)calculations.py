def calculations(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 // num2
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2

oper = input()
number1 = int(input())
number2 = int(input())

print(calculations(oper, number1, number2))
