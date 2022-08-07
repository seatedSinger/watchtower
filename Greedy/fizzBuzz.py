def fizzBuzz(n):
    res = range(1, n + 1)
    return ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x) for x in res]


# print(fizzBuzz(3))
# print(fizzBuzz(15))

# Adding complexity : Div by 7, 3 and 7, 3 and 5 and 7 etc..
# in this if divisible by 7 -> Print "Jazz"
def solution2(n):
    res = []
    for num in range(1, n + 1):
        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)
        divisible_by_7 = (num % 7 == 0)
        
        num_ans_str = ""

        if divisible_by_3:
            # divides by 3
            num_ans_str += 'Fizz'
        if divisible_by_5:
            num_ans_str += 'Buzz'
        if divisible_by_7:
            num_ans_str += 'Jazz'
        if not num_ans_str:
            # not divisible byt 3 or 5
            num_ans_str = str(num)
        res.append(num_ans_str)
    return res


print(solution2(15))
