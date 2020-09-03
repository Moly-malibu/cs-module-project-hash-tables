class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        result = ''
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        letter_location = {}
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                c = board[row][col]
                letter_location[c] = (row, col)
                
        row, col = 0, 0
        
        for letter in target:   # "mrzx"
            dest_row, dest_col = letter_location[letter]
            
            diff_row = dest_row - row
            diff_col = dest_col - col
            
            if diff_row > 0:
                vertical_direction = 'D' * diff_row
            elif diff_row < 0:
                vertical_direction = 'U' * -diff_row
                
            if diff_col > 0:
                horizontal_direction = 'R' * diff_col
            elif diff_col < 0:
                horizontal_direction = 'L' * -diff_col
                
            row += diff_row
            col += diff_col
            
            result += vertical_direction + horizontal_direction + '!'
            
        return result