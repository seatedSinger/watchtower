'''
bitwise | checking 33 bits
O(log n) | O(n)
'''

def divide(x, y):
    res = 0
    xx, yy = abs(x), abs(y)
    for i in range(32, -1, -1):
        if xx >= (yy << i):
            xx -= (yy << i)
            res += (1 << i)

    if (x > 0 and y < 0) or (x < 0 and y > 0):
        res = -res

    return min(2**31-1, max(-2**31, res))

a = 10
b = 3
print(divide(a,b))

a = 7
b = -3
print(divide(a,b))

a = 0
b = 1
print(divide(a,b))