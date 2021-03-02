
#* O(n) | O(1)

def solution(key, word):
    res = 0
    prev_pos = 0
    idx_map = {c:i for i, c in enumerate(key)}
    for i in word:
        res += abs(idx_map[i] - prev_pos)
        prev_pos = idx_map[i]
    return res


key = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(solution(key, word))

key = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
print(solution(key, word))
