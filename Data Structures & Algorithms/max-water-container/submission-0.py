class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0 
        left, right = 0, len(heights) - 1

        while left < right: 
            width = abs(left - right) 

            if heights[left] > heights[right]: 
                length = heights[right] 
                right -= 1
            else: 
                length = heights[left] 
                left += 1
            
            result = max(result, length * width) 


        return result  