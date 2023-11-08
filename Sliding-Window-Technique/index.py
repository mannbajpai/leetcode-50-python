
def maxSum(arr,windowSize):
    arrSize = len(arr)
    if arrSize < windowSize:
        return -1

    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum

    for i in range(arrSize - windowSize):
        window_sum = window_sum - arr[i] + arr[i+windowSize]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [80, -50, 40, 30, -20, 90, 100]
k = 3
answer = maxSum(arr, k)

print(answer)
