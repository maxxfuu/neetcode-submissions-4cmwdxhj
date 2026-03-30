class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    threshold = len(nums) / 2
    hashmap = {} # value, frequency 
    majority = nums[0] # psuedo number         

    for value in nums:
      hashmap[value] = hashmap.get(value, 0) + 1
      if hashmap[value] > threshold and hashmap[value] > hashmap[majority]:
        majority = value
    
    return majority 

