boxes = "001011"
boxes1 = "110"

# O(N^2)
def minOperationBoxes(boxes):
    res = [0] * len(boxes)
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxes[j] == '1':
                res[i] += abs(j - i)
    return res

print(minOperationBoxes(boxes))
print(minOperationBoxes(boxes1))

# OPTIMAL
def minOperation(boxes):
    pass

print(minOperation(boxes))
