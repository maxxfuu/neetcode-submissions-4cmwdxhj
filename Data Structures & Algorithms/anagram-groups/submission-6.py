class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char) - ord('a')] += 1
            
            hashmap[tuple(key)].append(word)

        result = [] 
        for o in hashmap.values():
            result.append(o)
        
        return result