class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                prev1, prev2 = res[-1]
                if prev1 <= interval[0] <= prev2:
                    res.pop() 
                    overlap = [prev1, max(prev2, interval[1])]
                    res.append(overlap)
                else:
                    res.append([interval[0], interval[1]])
            
        return res