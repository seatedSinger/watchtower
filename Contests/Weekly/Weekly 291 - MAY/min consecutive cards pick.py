'''
You are given an integer array cards where cards[i] represents the value of the ith card.
A pair of cards are matching if the cards have the same value.
Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards.
If it is impossible to have matching cards, return -1.

'''
# running slow

def minCardPickup(cards):
    seen, res = {}, float("inf")
    L, R = 0, 0
    smallest_card = float("inf")
    while L < len(cards) and R < len(cards):
        c = cards[R]
        if c in seen:
            L = seen[c] + 1
            res = min(res, R - L)
        seen[c] = R
        R += 1
    return -1 if res == float("inf") else res + 1


print(minCardPickup([3, 4, 2, 3, 4, 7]))
print(minCardPickup([1, 0, 5, 3]))
print(minCardPickup(["9, 4, 5, 6, 7, 5, 2"]))
