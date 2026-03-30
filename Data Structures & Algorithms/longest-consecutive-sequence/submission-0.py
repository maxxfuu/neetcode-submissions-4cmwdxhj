class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        longestSequence = 0 
        for i in numSet: 
            if i - 1 not in numSet: 
                # If it doesn't have a left neighbor then it is a start of a sequence 
                length = 0 
                while i + length in numSet: 
                    length += 1
                longestSequence = max(length, longestSequence)
        return longestSequence

       