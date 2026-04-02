class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i starts at 0, j starts at i + 1 
        # for each iteration i and j checks if they are the same
            # while i and j is the same then j discards inplace and everything shifts down 
        # in the end return the length of the array 

        i, j = 0, 1
        while j <= len(nums) - 1:
            print(i, j)
            if nums[i] == nums[j]:
                nums.remove(nums[j])
            else:
                i += 1
                j += 1
        
        return len(nums)


