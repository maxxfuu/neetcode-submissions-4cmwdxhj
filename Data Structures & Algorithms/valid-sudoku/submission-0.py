class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen_set = set()  
            for element in row:  # Use 'element' consistently
                if element != '.':  # Ignore empty cells
                    if element in seen_set:  # If element already exists, invalid sudoku
                        return False
                    seen_set.add(element)  # If element doesn't exist, add it

        # 2. Check for columns
        for index in range(9):  
            seen_set = set()  
            for row in board: 
                if row[index] != '.': 
                    if row[index] in seen_set:  # Duplicate found, invalid column
                        return False   
                    seen_set.add(row[index])  # Add element to set

        # 3. Check for 3x3 sub-boxes
        for box_row in range(0, 9, 3):  # Start at row 0, 3, 6
            for box_col in range(0, 9, 3):  # Start at column 0, 3, 6
                seen_set = set()  # Reset for each 3x3 box
                for i in range(3):
                    for j in range(3):
                        element = board[box_row + i][box_col + j]
                        if element != '.':  # Ignore empty cells
                            if element in seen_set:  # Duplicate found
                                return False
                            seen_set.add(element)  # Add element to set
        return True  # All checks passed; valid Sudoku
        
