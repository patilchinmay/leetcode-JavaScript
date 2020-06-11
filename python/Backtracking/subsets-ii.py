# https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        answer = []
        
        self.backtrack(0, path, answer, nums)
        return set(answer)
    
    def backtrack(self, index, path, answer, nums):
        if index == len(nums):
            answer.append(tuple(sorted(path).copy()))
            return
        
        path.append(nums[index])
        self.backtrack(index+1, path, answer, nums)
        
        path.pop()
        self.backtrack(index+1, path, answer, nums)