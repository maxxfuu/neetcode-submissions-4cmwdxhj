class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            numSet = set()
            for j in range(len(board)):
                c = board[i][j]
                if c in numSet:
                    return False
                elif c == '.':
                    continue   
                numSet.add(board[i][j])

        for i in range(len(board)):
            numSet = set()
            for j in range(len(board)):
                c = board[j][i]
                if c in numSet:
                    return False
                elif c == '.':
                    continue
                numSet.add(board[j][i])
        
        # Check each 3x3 sub-grid
        for r in range(0, 9, 3):       # Steps: 0, 3, 6 (top row of each block)
            for c in range(0, 9, 3):   # Steps: 0, 3, 6 (left col of each block)
                
                numSet = set()         # Reset the set for EVERY new 3x3 block
                for i in range(3):     # Row offset inside the block
                    for j in range(3): # Column offset inside the block
                        val = board[r + i][c + j]
                        
                        if val == ".": 
                            continue   # Skip empty cells
                        
                        if val in numSet:
                            return False
                        numSet.add(val)

        return True         