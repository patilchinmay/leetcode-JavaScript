# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        
        ans=[]
        if n%2 == 0:
            for i in range(n//2):
                ans.append(i+1)
                ans.append((i+1)*-1)
        else:
            for i in range(n//2):
                ans.append(i+1)
                ans.append((i+1)*-1)
            ans.append(0)
        
        return ans