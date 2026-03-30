class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        res = []

        def backTrack(idx, comb):
            if len(comb) == len(digits):
                if not digits:
                    return
                res.append(comb)
                return

            digit = digits[idx] # Input: 23, digit = 2, 3

            for i in range(len(hashmap[digit])): # list: [d, e, f], length = 3, itr: 0, 1, 2 
                comb += hashmap[digit][i]
                backTrack(idx + 1, comb)
                comb = comb[:len(comb) - 1]

        backTrack(0, "")
        return res
        
    
    
