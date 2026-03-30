class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(row: int, col: int) -> None:
      queue = collections.deque()
      visited.add((row, col))
      queue.append((row, col))
      
      while queue:
        row, col = queue.popleft()
        possible_directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr, dc in possible_directions:
          r, c = row + dr, col + dc

          if (r in range(rows) and 
              c in range(cols) and 
              (r, c) not in visited and  
              grid[r][c] == "1"):
            queue.append((r, c))
            visited.add((r, c))

    for row in range(rows):
      for col in range(cols):
        if grid[row][col] == "1" and (row, col) not in visited:
          bfs(row, col)
          islands += 1
    
    return islands
