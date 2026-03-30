class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        while left < right: 
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]: 
                right = mid 
            else: 
                left = mid + 1

        return nums[left]
        
        # result = nums[0]
        # left, right = 0, len(nums) - 1

        # while left < right: 
        #     if nums[left] < nums[right]: 
        #         return min(result, nums[left]) 

        #     mid = left + (right - left) // 2
        #     result = min(nums[mid], result)
        #     if nums[mid] >= nums[left]: 
        #         left = mid + 1
        #     else: 
        #         right = mid - 1
        # return result 



        # return min(nums) 