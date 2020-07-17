# https://leetcode.com/problems/out-of-boundary-paths/submissions/

class Solution:    
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
                
        answer = self.dfs(m, n, N, i, j, {})
        
        return answer % 1000000007
    
    def dfs(self, m, n, N, i, j, cache):
        # Define boundaries and conditions
        
        if not (0 <= i < m and 0 <= j < n):
            return 1
        
        if N == 0:
            return 0
        
        if (i,j,N) in cache:
            return cache[(i,j,N)]
        
        answer = 0
        
        answer += self.dfs(m, n, N-1, i+1, j, cache)
        answer += self.dfs(m, n, N-1, i-1, j, cache)
        answer += self.dfs(m, n, N-1, i, j+1, cache)
        answer += self.dfs(m, n, N-1, i, j-1, cache)
            
        cache[(i,j,N)] = answer
        
        return answer