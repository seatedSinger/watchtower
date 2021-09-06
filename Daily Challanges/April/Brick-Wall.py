'''
Find Edge with highest frequency in the wall
Number of Bricks Crossed by Line = Number of Rows in Wall - Frequency of Most Occuring Edge
So:
Number of Bricks Crossed by Line = Number of Rows in Wall - Frequency of Most Occuring Edge
=> Number of Bricks Crossed by Line = 6 - 4
=> Number of Bricks Crossed by Line = 2 (We return this answer)
'''
from collections import defaultdict

wall = [[1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]]

wall2 = [[1],
         [1],
         [1]]


def wallAndBricks(wall):
    freq = defaultdict(int)
    # aux = {}
    max_edges = 0
    for layer in wall:
        # LeftMost wall Pos = 0
        pos = 0
        # Not including RightMost
        for brick in layer[:-1]:
            pos += brick
            freq[pos] += 1
            max_edges = max(max_edges, freq[pos])
    return len(wall) - max_edges


def solution2(wall):
    freq = {}
    for bricks in wall:
        bricksEndPoint = 0
        for i in range(len(bricks) - 1):
            bricksEndPoint += bricks[i]
            freq[bricksEndPoint] = freq.get(bricksEndPoint, 0) + 1
    count = freq.values()
    return len(wall) - (max(count) if count else 0)


print(wallAndBricks(wall))
print(solution2(wall))
print(solution2(wall2))
