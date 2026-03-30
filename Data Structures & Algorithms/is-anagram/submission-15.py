class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)): return False

        HashMap = {} # Key: Char Value: Int

        for char in s: 
            if (char not in HashMap): 
                HashMap[char] = 1
            else:
                HashMap[char] += 1

        for char in t: 
            if (char in HashMap):
                HashMap[char] -= 1

        for i in HashMap: 
            if HashMap[i] != 0:
                return False

        return True
            
        







        