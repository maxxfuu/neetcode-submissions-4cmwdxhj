# base case: if currVal is greater than target or equal to target 
# sub problem: for each integer element, only find a combination with other integers after its range

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() 

        def backTrack(idx: int, currVals: List[int]):
            temp = sorted(currVals)
            if sum(currVals) == target and temp not in res:
                res.append(temp)
                return
            
            if sum(currVals) > target:
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev: # skip duplicates, go to the next iteraton
                    continue
                
                if candidates[i] + sum(currVals) > target: # prune early if greater than target
                    break

                currVals.append(candidates[i])
                backTrack(i + 1, currVals)
                currVals.pop()
                prev = candidates[i] # store previous candidates 

        backTrack(0, [])
        return res