# https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/

class Solution:
    def findLength(self, A: [int], B: [int]) -> int:
        rows = len(A) + 1
        cols = len(B) + 1
        
        dp = [ [0]*cols for _ in range(rows)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
        # print([row for row in dp])
        
        return max([max(row) for row in dp])