'''
Area = len of shorter vertical line * distance between lines
'''

def maxArea(height):
    i, j = 0, len(height) - 1
    res = 0
    while i <= j:
        area = min(height[i], height[j]) * (j - i)
        res = max(res, area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
height = [1, 1]
print(maxArea(height))
height = [1, 3, 2, 0, 2, 5, 4, 1, 2]
print(maxArea(height))
