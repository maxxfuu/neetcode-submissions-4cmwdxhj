class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True: 
            curr = ''
            for s in strs:
                if i > len(s) - 1:
                    return s[0:i]
                elif curr == '':
                    curr = s[i]
                elif s[i] != curr:
                    return s[0:i]
            i += 1

        return s[0:i+1]
