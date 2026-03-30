class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            difference = target - value

            for i in range(index): 
                if nums[i] == difference and i != index:
                    return [i, index]

            
            

                

        