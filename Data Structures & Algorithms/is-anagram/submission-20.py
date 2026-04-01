class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for sChar, tChar in zip(s, t):
            freqS[sChar] += 1
            freqT[tChar] += 1
        
        return freqS == freqT
