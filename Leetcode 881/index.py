class Solution:
    def numRescueBoats(self, people: [int], limit: int) -> int:

        people.sort()
        left = 0
        right = len(people) - 1
        num_of_boats = 0

        while left <= right:
            if left == right:
                num_of_boats = num_of_boats+1
                break
            elif people[left] + people[right] <= limit:
                left = left+1

            num_of_boats = num_of_boats+1
            right -= 1

        return num_of_boats




