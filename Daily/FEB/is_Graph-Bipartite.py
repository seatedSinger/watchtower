from collections import deque

graph = [[1,3],[0,2],[1,3],[0,2]]

def isBipartite(graph):
    seen = {}
    for i in range(len(graph)):
        if i not in seen:
            if check(graph, i, seen) == False:
                return False
    return True

def check(graph, start, seen):
    q = deque()
    q.append((start, 1))

    while q:
        node, color = q.popleft()

        if node in seen:
            if seen[node] != color:
                return False
            continue
        seen[node] = color

        for i in graph[node]:
            q.append((i, -color))
    return True