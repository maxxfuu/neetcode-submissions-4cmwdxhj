class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # Left and Right Pointer

        while left <= right:
            mid = (right + left) // 2
            print(nums[mid])
            if (nums[mid] < target): 
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                return mid
            
        return -1
        
