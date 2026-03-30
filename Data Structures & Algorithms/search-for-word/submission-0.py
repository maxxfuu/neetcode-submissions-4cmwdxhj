class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set() 

        def dfs(r, c, i) -> bool: 
            if (r < 0 or c < 0 or r == rows or c == cols or 
                (r, c) in visited or board[r][c] != word[i]):
                return False

            if i == len(word) -1 and board[r][c] == word[i]:
                return True

            visited.add((r, c))
            found = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.remove((r, c)) # needed to add remove 
            return found
         
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
