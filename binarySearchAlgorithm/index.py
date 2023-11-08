
def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1

    while l<=r:
        mid = (l+r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1

    return -1


arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target)

if result != -1:
    print("Element is present at index %d"% result)
else:
    print("Element is not present.")
