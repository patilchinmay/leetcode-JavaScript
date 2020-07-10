# https://leetcode.com/problems/surrounded-regions/submissions/

class Solution:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        The idea is to traverse (dfs) from all the 'O's on the edge of the matrix and mark the reachable 'O's inside as 'Z'.
        once the matrix is traversed, It will have 'X', 'Z' and 'O'.
        'O's are the ones that are not reachable from edges (also means that they are surrounded by 'X's). We mark them as 'X'
        'Z' are previously 'O's, that are reachable from edges. We mark them back as 'O'
        """
        if not board:
            return []
        
        if not board[0]:
            return [[]]
        
        # First and last row
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.dfs(0, i, board)
            if board[-1][i] == 'O':
                self.dfs(len(board)-1, i, board)
        
        # First and last column 
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][-1] == 'O':
                self.dfs(i, len(board[0])-1, board)
        
        # Switch up Characters
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'
            
    def dfs(self, i, j, board):
        
        # Define the boundaries and condition
        if not ( 0 <= i < len(board) and 0 <= j < len(board[0]) ):
            return
        
        if board[i][j] != 'O':
            return
        
        # Process the node
        board[i][j] = 'Z'
        
        # Call the neighbours
        self.dfs(i+1, j, board)
        self.dfs(i-1, j, board)
        self.dfs(i, j+1, board)
        self.dfs(i, j-1, board)