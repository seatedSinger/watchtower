#Number Guesing

def numberGuess(n):
    first = 0
    last = len(n)-1

    while first <= last:
        mid = (last + first)//2
        res = guess(mid)

        if res == 0:
            return mid
        elif res < 0:
            last = mid - 1
        else:
            first = mid + 1
    return -1

print(numberGuess(10))
'''
-1 : My number is lower
1 : My number is higher
0 : Congrats! You got it!

Here "My" means the number which is given for you to guess not the number you put into guess()
'''

def guess(num):
    pass
def guessNumber(self, n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if guess(mid) == 1:
            lo = mid + 1
        else:
            hi = mid
    return lo