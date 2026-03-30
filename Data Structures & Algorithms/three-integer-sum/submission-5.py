class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        seen = set()
        nums.sort() 
        result = []
        
        for i in range(len(nums)): 

            left, right = i + 1, len(nums) - 1
            target = nums[i] * -1 

            while left < right:
                current_sum = nums[left] + nums[right] 
                if current_sum < target: 
                    left += 1
                elif current_sum > target: 
                    right -= 1
                else: 
                    # target == current_sum  
                    triplet = [nums[i], nums[left], nums[right]] 
                    triplet.sort()
                    triplet = tuple(triplet) 

                    if triplet not in seen:  
                        seen.add(triplet) 
                        result.append(list(triplet)) 
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 
        return result  