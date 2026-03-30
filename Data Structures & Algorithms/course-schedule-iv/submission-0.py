class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hashmap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            hashmap[a].append(b)

        res = []
        memo = {}
        def dfs(node, target):
            visited = set()
            if (node, target) in memo:
                return memo[(node, target)]

            if node == target:
                memo[(node, target)] = True
                return memo[(node, target)]

            if node in visited:
                return False

            visited.add(node)
            for adj in hashmap[node]:
                if dfs(adj, target):
                    return True

            visited.remove(node)

            memo[(node, target)] = False
            return False 

        for u, v in queries:
            res.append(dfs(u, v))

        return res