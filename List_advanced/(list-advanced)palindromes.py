words = input().split()
repeat_word = input()

palindromes = [word for word in words if word == word[::-1]]
print(palindromes)
occ = palindromes.count(repeat_word)
print(f'Found palindrome {occ} times')