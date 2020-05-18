# https://leetcode.com/problems/counting-bits/submissions/

class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        
        for x in range(num+1):
            ans.append(bin(x).count('1'))
        
        return ans