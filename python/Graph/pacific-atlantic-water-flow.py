# https://youtu.be/LVlihRYfVVw?t=803
# https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        pacific = [ [0]*cols for _ in range(rows)]
        atlantic= [ [0]*cols for _ in range(rows)]
        
        # First and Last Column
        for i in range(rows):
            self.dfs(i, 0, -1, matrix, pacific)
            self.dfs(i, cols-1, -1, matrix, atlantic)
            
        # First and Last Row
        for i in range(cols):
            self.dfs(0, i, -1, matrix, pacific)
            self.dfs(rows-1, i, -1, matrix, atlantic)
        
        ans = []
        
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i,j])
                    
        return ans
    
    def dfs(self, row, col, parent_val, matrix, ocean):
        # Check the boundaries
        if not ( 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) ):
            return
        
        # Don't visit an already visited node
        if ocean[row][col] == 1:
            return
        
        # Don't visit node with value less than parent_val
        if matrix[row][col] < parent_val:
            return
        
        # Process the node. Mark is visited in respective ocean
        ocean[row][col] = 1
        
        # call the neighbours
        self.dfs(row+1, col, matrix[row][col], matrix, ocean)
        self.dfs(row-1, col, matrix[row][col], matrix, ocean)
        self.dfs(row, col+1, matrix[row][col], matrix, ocean)
        self.dfs(row, col-1, matrix[row][col], matrix, ocean)