# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

class Solution():
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(len(board)):
            chunk = [board[x][y] for x in [(i/3)*3, (i/3)*3+1, (i/3)*3+2] for y in [(i%3)*3, (i%3)*3+1, (i%3)*3+2]]
            if not self.isValid(chunk):
                return False
        for i in xrange(len(board)):
            if not self.isValid(board[i]):
                return False
        for i in xrange(len(board)):
            row = [board[x][i] for x in xrange(9)]
            if not self.isValid(row):
                return False
        return True

    def isValid(self, list):
        number = range(10)
        for x in list:
            if x != '.':
                try:
                    number.remove(int(x))
                except :
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    A = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    A = [".........","4........","......6..","...38....",".5...6..1","8......6.",".........","..7.9....","...6....."]
    print s.isValidSudoku(A)