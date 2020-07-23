# https://leetcode.com/problems/champagne-tower/submissions/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * i for i in range(1, 102)]
        
        tower[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                
                spill_over = (tower[row][col] - 1) / 2
                
                if spill_over > 0:
                    tower[row+1][col] += spill_over
                    tower[row+1][col+1] += spill_over
        
        # print(tower)
        
        return min(1, tower[query_row][query_glass])