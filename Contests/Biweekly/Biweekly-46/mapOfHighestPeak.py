from collections import deque

isWater = [[0,1],[0,0]]
isWater2 = [[0,0,1],[1,0,0],[0,0,0]]

#* Like a matrix
#? why BFS

'''
According to problem requirement, need to assign value of 0 to all waters;
- all land and neigh waters have a value of at most 1;
- all lands neigh lands with value of 1 will have a value at most 2;
- all lands neigh lands with a value of 2 will have a value of 3 at most;
'''

def highestPeak(isWater):
    # m, n = map(len, (isWater, isWater[0]))
    m, n = len(isWater), len(isWater[0])
    dq = deque([])
    heights = [[-1] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if isWater[r][c] == 1:
                heights[r][c] = 0
                dq.append((r, c))
    # DIR = [0, 1, 0, -1, 0]
    while dq:
        for _ in range(len(dq)):
            r, c = dq.popleft()

            for x, y in (r, c+1), (r,c-1), (r+1,c), (r-1, c):
                if m > x >= 0 <= y < n and heights[x][y] < 0:
                    heights[x][y] = heights[r][c] + 1
                    dq.append((x, y))
    return heights


print(highestPeak(isWater2))
