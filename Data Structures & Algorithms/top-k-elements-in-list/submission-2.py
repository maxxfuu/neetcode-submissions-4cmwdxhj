class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        sortedHashMap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sortedHashMap[i][0])

        return result