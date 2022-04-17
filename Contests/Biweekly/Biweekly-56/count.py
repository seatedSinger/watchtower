#Count Square Sum Triples
def countTriples(n):
    res = 0
    sq = set([i**2 for i in range(1, n + 1)])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = i**2 + j**2
            if x in sq:
                res += 1
    return res
