nums = [4, 2, 3]
nums2 = [4, 2, 1]
nums3 = [12, 9, 10, 5, 2]


def checkPossiblity(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            print(nums[i])
            count += 1
            if i > 0:
                if nums[i + 1] < nums[i - 1]:
                    # HERE
                    print(nums[i + 1], nums[i - 1])
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
    return count <= 1


print(checkPossiblity(nums3))
