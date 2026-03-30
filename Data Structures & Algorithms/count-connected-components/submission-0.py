class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i: [] for i in range(n)}
        visited = set() 
        count = 0

        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        def dfs(node):
            stack = [node]
            visited.add(node)
            while stack:
                node = stack.pop()
                for neighbor in hashmap[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor) 
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count  