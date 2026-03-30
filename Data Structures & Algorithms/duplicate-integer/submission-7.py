class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use Set to check for uniqueness later 
        seen = set()
        for i in nums: 
            if (i in seen): 
                return True 
            else: 
                seen.add(i) 

        return False