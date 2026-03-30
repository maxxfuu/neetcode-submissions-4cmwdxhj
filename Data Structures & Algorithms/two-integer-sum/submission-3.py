class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      # HashMap Solution
      HashMap = {}

      for i, num in enumerate(nums): 
        diff = target - num
        if (diff in HashMap): # Check if Key exists. 
          return [HashMap[diff], i]
        else:
          HashMap[num] = i 
      
      return []
      
      # Brute Force Solution 
      # for index, value in enumerate(nums): 
      #   diff = target - value

      #   for i in range(len(nums)):
      #     if (nums[i] == diff and i != index): 
      #       return [i, index] 