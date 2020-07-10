# https://leetcode.com/problems/sqrtx/submissions/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left = 1
        right = x // 2
        
        ans = 0
        
        while left <= right:
            
            mid = left + (right-left) // 2
            
            if mid*mid == x:
                ans = mid
                break
            elif mid*mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # print(ans, left, right)
        
        return right if ans == 0 else ans