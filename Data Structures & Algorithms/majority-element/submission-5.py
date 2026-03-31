class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        res = nums[0] 

        for key, freq in hashmap.items():
            if freq > hashmap[res]:
                res = key

        return res
