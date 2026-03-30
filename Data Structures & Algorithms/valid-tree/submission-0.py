class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 0:
            return False
        if n == 1:
            return True
        
        hashmap = {i: [] for i in range(n)} 
        visited = set()
        length = len(edges) + 1

        if edges == []:
            if n == 1:
                return True 
            return False 
        
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        print(hashmap)

        def dfs(node, prevNode, hashmap, visited):
            if hashmap[node] == []:
                return True

            if node != prevNode and node in visited:
                print(prevNode, node)
                return False 

            visited.add(node)
            for neighbor in hashmap[node]: 
                if neighbor == prevNode:
                    continue

                if dfs(neighbor, node, hashmap, visited) == False:
                    return False

            return True

        if not dfs(0, None, hashmap, visited):
            return False

        return len(visited) == length