class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Sliding Window, counter for the length of s1. left and right pointer in the 
        # direction. Assume left and right is on the same index. If the current char is 
        # part of the possible characters in the substring, then we shift the right pointer
        # and continue to check. If it is a character we increment a counter. If the char 
        # does not exists when the counter hasn't reached the end, we shift the left pointer 
        # to the right pointer and continue to check until the end. 

        s1_seen, window_seen = {}, {} 

        # Edge Case 
        if len(s1) > len(s2): 
            return False 

        # populate the frequency map  
        for char in s1: 
            s1_seen[char] = s1_seen.get(char, 0) + 1 
        
        # Static Sliding Window
        left = 0 
        for right in range(len(s2)): 
            if s2[right] in window_seen: 
                window_seen[s2[right]] += 1
            else: 
                window_seen[s2[right]] = 1

            # If window is too big 
            if right - left + 1 > len(s1): 
                if window_seen[s2[left]] == 1: 
                    del window_seen[s2[left]] 
                else: 
                    window_seen[s2[left]] -= 1
                left += 1 
            
            if window_seen == s1_seen: 
                return True 

        return False 
        