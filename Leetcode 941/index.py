from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1

        if i == 1 or i == len(arr):
            return False

        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1

        return i == len(arr)




s= Solution()
res = s.validMountainArray([0,2,4,5,6,7,9,6,5,4,3,2])
print(res)
