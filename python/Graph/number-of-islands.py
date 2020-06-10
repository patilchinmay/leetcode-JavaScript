# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i,j, grid)
                    count += 1
        
        return count
    
    def dfs(self, row, col, grid):
        # Check the conditions
        
        # validate the indices
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        # validate the node value
        if grid[row][col] == '0':
            return
        
        # Process the node
        grid[row][col] = '0'
        
        # Call the neighbours
        self.dfs(row - 1, col, grid)
        self.dfs(row + 1, col, grid)
        self.dfs(row, col - 1, grid)
        self.dfs(row, col + 1, grid)