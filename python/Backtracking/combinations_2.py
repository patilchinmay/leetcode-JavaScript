# https://leetcode.com/problems/combinations/submissions/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        
        answer = combinations([i+1 for i in range(n)], k)
        
        return answer