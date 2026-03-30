class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs: 
            count = [0] * 26
            for char in word: 
                count[ord(char) - ord("a")] += 1 # get the positon of the char based on ASCII

            result[tuple(count)].append(word) 
        return list(result.values()) 