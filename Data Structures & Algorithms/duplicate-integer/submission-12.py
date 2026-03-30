class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        my_set = set([])  
        for i in range(len(nums)): 
            if nums[i] not in my_set: 
                my_set.add(nums[i])
            else: 
                return True
        return False 