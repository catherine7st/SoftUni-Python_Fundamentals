def factorial_calculator(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result


num1 = int(input())
num2 = int(input())

fact_num1 = factorial_calculator(num1)
fact_num2 = factorial_calculator(num2)

final_result = fact_num1 / fact_num2
print(f'{final_result:.2f}')

