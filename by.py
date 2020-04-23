def searchBinary(l2s, sval):  # do not use 'list' as a variable
    low = 0
    high = len(l2s)

    while low <= high:  # this is the main issue. As long as low is not greater than high, the while loop must run
        mid = (high + low) // 2

        if l2s[mid] == sval:
            print("found : ", sval)
            return
        elif l2s[mid] > sval:
            high = mid - 1
        else:
            low = mid + 1


list_ = [1, 2, 3, 4, 6]
print(searchBinary(list_, 1))
#########
def new_branch(val):
    i = 0
    j = len(val)-1
    prah = []
    while i < j:
        if val[i]  == val[i+1]:
            prah.append(val[i])
    for val in enumerate(list_,start=1):
        pass