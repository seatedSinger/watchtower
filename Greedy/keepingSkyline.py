'''
807.Max Increase to Keep City Skyline
'''

def maxKeepingSkyline(grid):
    maxes = [max(col) for col in zip(*grid)]
    return maxes


print(maxKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
