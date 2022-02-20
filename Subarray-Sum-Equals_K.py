def sumSubarray(nums, k):
    auxSum = {0: 1}
    # since initially you have 0 with occurence 1
    currSum = 0
    res = 0
    for i in nums:
        currSum += i  # prefix sum
        # Accumulate can be Used ( itertools )
        res += auxSum.get(currSum - k, 0)  # Taking difference
        auxSum[currSum] = auxSum.get(currSum, 0) + 1
    return res

print(sumSubarray([9, 4, 20, 3, 10, 5], 33))
