class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        mid = left + (right - left) // 2

        while (right >= left and nums[mid] != target):  
            if target > nums[mid]: 
                left = mid + 1 
                mid = left + (right - left) // 2
            elif target < nums[mid]: 
                right = mid - 1
                mid = left + (right - left) // 2 

        return mid if nums[mid] == target else -1  
