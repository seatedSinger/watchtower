'''
Digital root formula:
dr**10(n) == 0, if n == 0
dr**10(n) == 9, if n == 9k
dr**10(n) == n mod 9, if n != 9k
"The original number is divisible by 9 if and only if the sum of its digits is divisible by 9".
'''

def addDigit(num):
    # num = str(num)
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


def solution_2(num):
    # dr**10(n) == 0, if n == 0
    # dr**10(n) == 1 + (n - 1) mod 9, if n != 0
    return 1 + (num - 1) % 9 if num else 0


print(addDigit(38))
print(solution_2(38))
