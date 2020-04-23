arr = [61,2,79,8,4,55]

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# print(bubble_sort(arr))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        pos = i
        current_value = arr[pos]

        while pos > 0 and arr[pos - 1] > current_value:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = current_value
    return arr

# print(insertion_sort(arr))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        item_greater = [item for item in arr if item > pivot]
        item_smaller = [item for item in arr if item <= pivot]

        return quick_sort(item_smaller)+[pivot]+quick_sort(item_greater)
# print(quick_sort(arr))
def binary_sort(arr,target):
    pass