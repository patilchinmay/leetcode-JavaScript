# https://leetcode.com/problems/powx-n/submissions/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        
        if n < 0: 
            x = 1/x
            n = -n
        
        ans = 1 
        curProd = x
            
        while (n > 0):
            
            if n % 2 == 1:
                ans *= curProd
                
            curProd *= curProd
            
            n //= 2
        
        return ans