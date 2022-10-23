class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_row(board) and self.check_column(board) and self.check_square(board)
    
    def check_row(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True
    
    def check_column(self, board):
        for column in zip(*board):
            if not self.is_valid(column):
                return False
        return True
    
    def check_square(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid(square):
                    return False
        return True
    
    def is_valid(self, block):
        block = [i for i in block if i != '.']
        return len(set(block)) == len(block)