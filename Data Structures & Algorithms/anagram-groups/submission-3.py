# 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            freq = [0] * 26
            for index, char in enumerate(word):
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
            
        return list(hashmap.values())
        

                