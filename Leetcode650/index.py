class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}

        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000
            if (count, paste) in cache:
                return cache[(count, paste)]

            # Pasting
            result1 = 1 + helper(count + paste, paste)

            # Copying & Pasting
            result2 = 2 + helper(count*2, count)

            cache[(count, paste)] = min(result1, result2)
            return cache[(count, paste)]
        if n == 1:
            return 0

        return 1 + helper(1, 1)
