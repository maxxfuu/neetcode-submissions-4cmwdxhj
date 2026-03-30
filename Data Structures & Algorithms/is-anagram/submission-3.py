class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The count of each character has to be the same for both strings

        # hashmap is esentially dictionary in python 
        # key: char, value: int 
         
        hash_map = {}
        
        if(len(s) != len(t)): 
            return False 

        for char1, char2 in zip(s, t): 
            if(char1 in hash_map): 
                hash_map[char1] += 1
            else: 
                hash_map[char1] = 1

            if(char2 in hash_map): 
                hash_map[char2]  -= 1
            else:
                hash_map[char2] = -1 

        for count in hash_map.values(): 
            if (count != 0): 
                return False 

        return True
        
    