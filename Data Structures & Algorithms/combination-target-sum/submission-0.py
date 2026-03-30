class Solution:
    # subproblem: for each node, iterate its range and allow duplicates
    # base case: if sum > target or index i reaches the end of the list
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, currVals: List[int]):
            if sum(currVals) == target:
                res.append(currVals.copy())
                return
            
            if sum(currVals) > target:
                return 
            
            for i in range(start, len(candidates)): # candidates = [2, 3, 5], length = 3, iterate: 0, 1, 2
                print(i)
                currVals.append(candidates[i])
                backtrack(i, currVals)
                currVals.pop()

        backtrack(0, [])
        return res