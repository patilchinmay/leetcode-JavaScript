# Explanation: https://www.youtube.com/watch?v=GuTPwotSdYw
# https://leetcode.com/problems/permutations/submissions/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.backtrack_and_swap(0, nums, answer)
        return answer
    
    def backtrack_and_swap(self, index, nums, answer):
        
        if index == len(nums):
            answer.append(nums)
            return

        for i in range(index, len(nums)):
            
            nums[index], nums[i] = nums[i], nums[index]
            
            self.backtrack_and_swap(index+1, list(nums), answer)
            
            nums[i], nums[index] = nums[index], nums[i]