def solution(items, ruleKey, ruleValue):
    map_ = {'type': 0, 'color': 1, 'name': 2}
    res = 0
    for i in items:
        if i[map_[ruleKey]] == ruleValue:
            res += 1
    return res

# return sum((ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)) for t, c, n in items)

items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(solution(items, ruleKey, ruleValue))

items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(solution(items, ruleKey, ruleValue))
