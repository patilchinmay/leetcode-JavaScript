# https://leetcode.com/problems/xor-operation-in-an-array/submissions/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        if n == 1:
            return start
        
        array = [start + 2 * index for index in range(n)]
        
        answer = array[0]
        
        for i in range(1, len(array)):
            answer = answer ^ array[i]
            
        return answer