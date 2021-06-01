s = "deeedbbcccbdaa"
k = 3


def removeDupes(s, k):
    stack = [['#', 0]]
    # stack = []
    for i in s:
        if stack and stack[-1][0] == i and stack[-1][1] + 1 == k:
            stack.pop()
        elif stack and stack[-1][0] == i:
            stack[-1][1] += 1
        else:
            stack.append([i, 1])
    # return stack
    return ''.join(i * j for i, j in stack)


print(removeDupes(s, k))


def solution2(s, k):
    stack = [['#', 0]]
    for i in s:
        if stack[-1][0] == i:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([i, 1])
    return ''.join(i * j for i, j in stack)


# print((solution2(s, k)))
