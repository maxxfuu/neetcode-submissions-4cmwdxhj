class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSet, currSet = [], []

        def helper(i, nums, currSet, subSet):
            if (i == len(nums)):
                subSet.append(currSet.copy())
                return
            
            # decision to include nums[i]
            currSet.append(nums[i])
            helper(i + 1, nums, currSet, subSet)

            # decision to not include nums[i]
            currSet.pop()
            helper(i + 1, nums, currSet, subSet)

        helper(0, nums, currSet, subSet)
        return subSet 
    
