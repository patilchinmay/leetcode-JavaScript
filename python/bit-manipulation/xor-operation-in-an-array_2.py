# https://leetcode.com/problems/xor-operation-in-an-array/submissions/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        if n == 1:
            return start
                
        answer = start
        
        for i in range(1, n):
            answer = answer ^ (start + 2 * i)
            
        return answer