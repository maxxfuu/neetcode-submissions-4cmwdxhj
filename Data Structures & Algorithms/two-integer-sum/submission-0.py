class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            target_value = target - nums[i]
            
            for j in range(len(nums)): 
                if(nums[j] == target_value and j != i):
                    return [i, j]
    

