# https://leetcode.com/problems/subsets/submissions/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        answer = []
        self.backtrack(0, path, nums, answer)
        return answer

    def backtrack(self, index, path, nums, answer):        
        if index == len(nums):
            answer.append(path.copy())
            return
                
        # include item at index
        path.append(nums[index])
        self.backtrack(index+1, path, nums, answer)
        
        # exclude item at index
        path.pop() # popping it because we have included it above. so it is similar to not including it
        self.backtrack(index+1, path, nums, answer)