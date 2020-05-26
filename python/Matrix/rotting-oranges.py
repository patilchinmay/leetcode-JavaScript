# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_oranges = 0
        queue = []
        minute = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_oranges+=1
                elif grid[i][j] == 2:
                    queue.append([i,j])
    
        if good_oranges == 0:
            return 0
        
        if not queue:
            return -1
        
        while queue:     
            for _ in range(len(queue)):
                [i,j] = queue.pop(0)

                for dir_ in dirs:
                    target_i = i + dir_[0]
                    target_j = j + dir_[1]

                    if 0 <= target_i < len(grid) and 0 <= target_j < len(grid[0]) and grid[target_i][target_j] == 1:
                        grid[target_i][target_j] = 2
                        queue.append([target_i, target_j])
            
            minute+=1
                
        fresh_orange_exist = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_orange_exist = True
                    break
        
        return -1 if fresh_orange_exist else minute-1