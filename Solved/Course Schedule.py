numCourses = 2
prerequisites = [[1, 0]]
numCourses_2 = 2
prerequisites_2 = [[1, 0], [0, 1]]
numCourses_3, prerequisites_3 = 5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]


def courseSchedule(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}
    print(preMap)
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    print(preMap)
    # visitSet =  all courses allong curr DFS path
    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


print(courseSchedule(numCourses_3, prerequisites_3))
        