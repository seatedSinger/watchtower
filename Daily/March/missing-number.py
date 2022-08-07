# O(n) | O(n)
# o(n) | O(1)

def solution(nums):
    aux = set(nums)
    for i in range(len(nums)+1):
        if i not in aux:
            return i


def solution2(nums):
    return len(nums)*(len(nums)+1)//2 - sum(nums)

