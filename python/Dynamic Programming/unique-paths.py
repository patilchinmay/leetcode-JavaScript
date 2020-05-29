# https://leetcode.com/problems/unique-paths/submissions/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create 2D array with first item in every row as 1
        dp = [ [1]+[0]*(n-1) for _ in range(m)]
        
        # All items in first row as 1
        for i in range(len(dp[0])):
            dp[0][i] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]