# last occurence for each letter in the string
'''
Scan through s via a stack. If the current character is not in stack, we pop out characters in stack
from the top that are larger than the current one and are still available later in s.
'''
# ANCHOR
def smallestSubq(s):
    last_occ = {x:i for i,x in enumerate(s)}
    # print(last_occ)
    stack = []
    for i, v in enumerate(s):
        if v not in stack:
            while stack and stack[-1] > v and i < last_occ[stack[-1]]:
                stack.pop()
            stack.append(v)
    return ''.join(stack)
    
'''
def smallestSubq(s):
    last = {c: i for i, c in enumerate(S)}
    stack = []
    for i, c in enumerate(S):
        if c not in stack:
        # if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
    return "".join(stack)
'''

s = 'bcabc'
print(smallestSubq(s)) 
s = 'cbacdcbc'
print(smallestSubq(s))
