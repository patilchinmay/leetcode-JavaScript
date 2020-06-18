# https://leetcode.com/problems/combination-sum/submissions/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        self.backtrack(path, ans, candidates, target)
        
        # print(ans)
        return ans
    
    def backtrack(self, path, ans, candidates, target):
        # boudaries and conditions
        if sum(path.copy()) > target:
            return
        
        if sorted(path) in ans:
            return
        
        if sum(path) == target:
            ans.append(sorted(path))
            return
        
        # Calling next possible combination
        for i in range(len(candidates)):
            path.append(candidates[i]) # Make a choice
            self.backtrack(path, ans, candidates, target)
            path.pop() # Backtrack