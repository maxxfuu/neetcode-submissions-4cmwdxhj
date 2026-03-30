class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        currSet, subSet = [], []
        nums.sort()

        def dfs(i, nums, currSet, subSet):
            if i == len(nums):
                subSet.append(currSet.copy())
                return 
            
            currSet.append(nums[i])
            dfs(i + 1, nums, currSet, subSet)

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            currSet.pop()
            dfs(i + 1, nums, currSet, subSet)
        
        dfs(0, nums, currSet, subSet)
        return subSet
