# import heapq
slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8


def meetingSchedule(s1, s2, d):
    # min_heap = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
    s1.sort(key=lambda x: x[0])
    s2.sort(key=lambda x: x[0])
    for i in range(len(s1) - 1):
        left = max(s1[i][0], s2[i][0])
        right = min(s1[i][1], s2[i][1])
        if left + d <= right:
            return [left, left + d]
    return []


def meetingSchedule2(s1, s2, d):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        left = max(s1[i][0], s2[i][0])
        right = min(s1[i][1], s2[i][1])
        if left + d <= right:
            return [left, left + d]
        if s1[i][1] < s2[j][1]:
            i += 1
        else:
            j += 1
    return []


print(meetingSchedule(slots1, slots2, duration))
print(meetingSchedule2(slots1, slots2, duration))
