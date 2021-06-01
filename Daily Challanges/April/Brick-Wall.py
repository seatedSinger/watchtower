'''
Line is Optimal HOW ?
Find Edge with highest frequency in the wall
'''
from collections import defaultdict

wall = [[1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]]


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


print(wallAndBricks(wall))
