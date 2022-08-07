'''
'''

def balancedString(s):
    count = 0
    res = 0
    for char in s:
        if char == 'R':
            count += 1
        if char == 'L':
            count -= 1
        res += count == 0
    #     count += char == 'L'
    #     count -= char == 'R'
    #     res += count == 0
    return res


print(balancedString("RLRRLLRLRL")) # 4
print(balancedString("RLRRRLLRLL")) # 5
