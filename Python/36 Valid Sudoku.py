# https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        colCheck = []
        rowCheck = []
        
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != "." and board[row][col] in rowCheck:
                    return False
                elif board[col][row] != "." and board[col][row] in colCheck:
                    return False
                else:
                    rowCheck.append(board[row][col])
                    colCheck.append(board[col][row])
            del rowCheck[:]
            del colCheck[:]

        # Block Check
        boxCheck = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                for x in range(i,i+3):
                    for y in range(j, j+3):
                        if board[x][y] != "." and board[x][y] in boxCheck:
                            return False
                        else:
                            boxCheck.append(board[x][y])
                del boxCheck[:]
        return True
                