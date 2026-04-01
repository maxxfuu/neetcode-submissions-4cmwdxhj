class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = defaultdict(int)
            freq = 0
            for j in range(i, len(s)):
                count[s[j]] += 1
                freq = max(freq, count[s[j]]) 

                window = j - i + 1 
                if window - freq <= k:
                    res = max(res, window)
                else:
                    break

        return res 
        

# ACBCAABC


        