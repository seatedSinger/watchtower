'''
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized.
The test cases are generated such that digit occurs at least once in number.

'''


def removeDigits(number, digit):
    num = []
    for i, val in enumerate(number):
        if val == digit:
            num.append(number[:i] + number[i+1:])
    return max(num)


print(removeDigits("1231", "1"))
print(removeDigits("551", "5"))
print(removeDigits("68281", "8"))
print(removeDigits("123", "3"))
