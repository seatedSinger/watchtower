'''
v & 1 means v % 2 == 1
& is a bitwise AND operation.
v & 1 produces a value that is either 1 or 0, depending on the least significant
bit of v: if the last bit is 1, the result of v & 1 is 1; otherwise, it is 0.
The value picked is "v & 1", i.e. 1 if the count is odd.
'''
from typing import Counter


def longestPalindrome(s):
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
        else:
            seen.remove(char)
    return len(s) - len(seen) + 1 if len(seen) > 0 else len(s)


print(longestPalindrome('abccccdd')) # 7
print(longestPalindrome('a'))
