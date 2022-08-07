costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]


def paintHouse(costs):
    if not costs:
        return 0
    for i in range(1, len(costs)):
        '''
        Why not consider previous | You're compring second with first
        and to check if that alternate painting connections are meet or
        not
        '''
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
    return min(costs[len(costs) - 1])


print(paintHouse(costs))
