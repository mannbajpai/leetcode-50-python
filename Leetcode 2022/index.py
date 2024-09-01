from typing import List
# Basic Solution
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        sol = []
        if len(original) != m*n:
            return []
        else :
            l = 0
            for i in range(m):
                row = []  # Create a new row for each iteration
                for j in range(n):
                    row.append(original[l])  # Append elements to the row
                    l+=1
                sol.append(row)  # Append the row to the solution

        return sol

# Optimized Code
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        return [original[i*n:(i+1)*n] for i in range(m)]
