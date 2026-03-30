class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() 
        
        # Check for Rows 
        for row in board: 
            for i in row: 
                if i not in seen:
                    if i != ".": 
                        seen.add(i)
                else: 
                    return False 
            seen = set() 

        # Check for Columns
        i = 0  
        for iter in range(9): 
            for row in board: 
                if row[i] not in seen: 
                    if row[i] != ".": 
                        seen.add(row[i])
                else:
                    return False 
            i += 1
            seen = set()
        

        # Check for 3x3 Grids
        for grid_row in range(0, 9, 3):  # Start indices of each 3x3 grid
            for grid_col in range(0, 9, 3):
                seen = set()
                for r in range(grid_row, grid_row + 3):
                    for c in range(grid_col, grid_col + 3):
                        if board[r][c] != ".":  # Ignore empty cells
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])

        return True 