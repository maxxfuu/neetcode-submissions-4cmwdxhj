class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # use a map to keep count of the frequency of the integers
       # iterate over the dict twice to find the max. 

        map = {} 
        elements = [] 
        num, count = 0, 0  

        for integer in nums: 
            if integer not in map:  
                map[integer] = 0
            else: 
                map[integer] += 1 
        
        while k > count:  
            num = max(map, key=lambda k: map[k]) 
            elements.append(num) 
            del map[num] 
            count += 1                        

        return elements