'''
O(N) | O(n)

- LinkedIn
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.
Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
'''
s = "xyxxxyxyy"


def minimumFlips(s):
    len_ = len(s)
    left = [0 for i in range(len_)]
    right = [0 for i in range(len_)]
    flips = 0
    for i in range(len(s)):
        if s[i] == 'y':
            flips += 1
        left[i] = flips

    flips = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'x':
            flips += 1
        right[i] = flips

    max_soFar = float('inf')
    for i in range(1, len(s)):
        max_soFar = min(max_soFar, left[i - 1] + right[i])
    return max_soFar


print(minimumFlips(s))
