class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        path = 0

        def bfs(row, col):
            queue = collections.deque()
            queue.append([0, 0])
            visited.add((0, 0))
            length = 1

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    if grid[row][col] == 1:
                        return -1
    
                    if row == rows - 1 and col == cols - 1:
                        return length 
    
                    possible_directions = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
                    for r, c in possible_directions:
                        if (row + r >= 0 and row + r < rows and col + c >= 0 and col + c < cols and
                            (row + r, col + c) not in visited and grid[row + r][col + c] == 0):
                            queue.append([row + r, col + c])
                            visited.add((row + r, col + c))
                length += 1
            return -1
            
        path = bfs(0, 0)
        return path 