class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1

        for index in range(len(nums)): 
            for i in range(len(nums)): 
                if index != i: 
                    product *= nums[i]
            output.append(product) 
            product = 1 
    
        return output 
