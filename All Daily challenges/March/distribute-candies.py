def solution(candies):
    unique_candies = len(set(candies))
    return min(len(candies)//2, unique_candies)


a = [1,1,2,2,3,3]
print(solution(a))

a = [1,1,2,3]
print(solution(a))

a = [6,6,6,6]
print(solution(a))
