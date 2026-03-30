class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # key: (i, currSum), value: ways 

        def dp(i: int, currSum: int):
            if i == len(nums):
                return 1 if currSum == target else 0

            if (i, currSum) in cache:
                return cache[(i, currSum)]

            ways = dp(i + 1, currSum + nums[i]) + dp(i + 1, currSum - nums[i])
            cache[(i, currSum)] = ways
            return ways
        
        return dp(0, 0)
        