# https://leetcode.com/problems/word-search/submissions/
# DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ans = False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Find all occurences of first character and run DFS from there according to our rules
                if board[i][j] == word[0]:
                    ans = ans or self.dfs(board, word, i, j, 0)
                    if ans:
                        return True
        return ans
    
    
    def dfs(self, board, word, i, j, index):
        # Base case rule to validate indices of grid/board
        if i < 0 or j < 0 or i > (len(board) - 1) or j > (len(board[i]) - 1):
            return False

        # If the character at required position is not the character we want, return False
        if board[i][j] != word[index]:
            return False
        
        # If the character at required position is what we want and we are at last position in word, return True
        if index == len(word) - 1:
            return True
        
        # Invalidating the parent character from encountering in neighbours
        char = board[i][j]
        board[i][j] = '*'
        
        # Recursive dfs with all 4 neighbours (i,j permutation) and index of word increased by 1
        ans = self.dfs(board, word, i+1, j, index+1) or self.dfs(board, word, i-1, j, index+1) or self.dfs(board, word, i, j+1, index+1) or self.dfs(board, word, i, j-1, index+1)
        
        # Restore the previosuly invalidated parent character
        board[i][j] = char
        
        return ans