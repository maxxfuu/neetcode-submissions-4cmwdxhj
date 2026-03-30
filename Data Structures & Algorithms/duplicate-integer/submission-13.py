class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for integer in nums: 
            if integer not in seen: 
                seen.add(integer) 
            else: 
                return True  
        return False  
