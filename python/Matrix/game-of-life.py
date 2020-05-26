# https://leetcode.com/problems/game-of-life/submissions/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """    
        board_copy = [i.copy() for i in board]
        
        rows = len(board)
        cols = len(board[0])
        
        dirs = [ [-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1] ] 
        
        for i in range(rows):
            for j in range(cols):
                # Neighbour count
                dead = 0
                live = 0
                
                # Check all 8 neighbours and store dead/live neighbour counts
                for dir_ in dirs:
                    # Validate indices
                    if 0 <= i+dir_[0] < rows and 0 <= j+dir_[1] < cols:
                        if board[i+dir_[0]][j+dir_[1]] == 0:
                            dead+=1
                        else:
                            live+=1
                
                # Four conditions follow from here.
                # Check the item in original board and make changes in copied board.
                # We will copy the copied board back into original one at the end.

                # Any live cell with fewer than two live neighbors dies
                if board[i][j] == 1  and live < 2:
                    board_copy[i][j] = 0
                
                # Any live cell with two or three live neighbors lives on to the next generation
                if board[i][j] == 1 and (live == 2 or live == 3):
                    pass
                
                # Any live cell with more than three live neighbors dies
                if board[i][j] == 1 and live > 3:
                    board_copy[i][j] = 0
        
                # Any dead cell with exactly three live neighbors becomes a live cell
                if board[i][j] == 0 and live == 3:
                    board_copy[i][j] = 1
        
        # copying the copied-board back into original one because we need to do in-place changes
        for i in range(rows):
            for j in range(cols):
                board[i][j] = board_copy[i][j]