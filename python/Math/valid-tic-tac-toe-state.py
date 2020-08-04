# https://leetcode.com/problems/valid-tic-tac-toe-state/submissions/

class Solution:
    def validTicTacToe(self, board: [str]) -> bool:        
        
        counts = {
            'X' : 0,
            'O' : 0,
            ' ' : 0
        }
        
        won = {
            'X': False,
            'O': False
        }
        
		# Learn the board and counts of each item
        for i in range(3):
            for j in range(3):
                counts[board[i][j]] += 1
            board[i] = list(board[i])
            # print(board[i])
        
        # print(counts)
        
		# Mathematical constraints for the game to be valid
        if counts['X'] + counts['O'] + counts[' '] != 9:
            return False
        
		# X plays before O, so O can not be greater than X ever.
        if counts['X'] < counts['O']:
            return False
        
		# Turns are alternate, so X and O can differ by at most 1.
        if counts['X'] > counts['O']+1:
            return False
        
		# Understand the winners, if any

		# Rows and Columns
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                won[board[i][0]] = True
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                won[board[0][i]] = True
        
		# Diagonal
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            won[board[1][1]] = True

		# Diagonal
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            won[board[1][1]] = True
        
        # print(won)
        
		# Both can not win
        if won['X'] and won['O']:
            return False
        
		# Match is drawn
        if not won['X'] and not won['O']:
            return True
        
		# Either has won
        if won['X'] != won['O']:
            # X plays first, so O will be 1 less if X wins
            if won['X']:   
                if counts['X'] - counts['O'] == 1:
                    return True
			
            # O plays second (catches up to the X's count), so X and O will be equal in number if O wins
            if won['O']:   
                if counts['O'] - counts['X'] == 0:
                    return True
            
            return False
        
'''
["XOX", "OXO", " XO"]
["OXX","XOX","OXO"]
["XOX","OOX","XO "]
'''