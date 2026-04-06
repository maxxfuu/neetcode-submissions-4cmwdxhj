class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] != 1:
                left = right + 1
            res = max(res, right - left + 1)

        return res 
             