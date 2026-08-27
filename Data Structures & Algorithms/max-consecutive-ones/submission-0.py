class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_consecutive = max(max_consecutive, current)
            else:
                current = 0

        return max_consecutive