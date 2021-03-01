def perfect_number(num):
    divisors = []
    for number in range(1, num):
       if num % number == 0:
           divisors.append(number)
    if sum(divisors) == num:
        return True
    return False


p_number = int(input())
if perfect_number(p_number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
