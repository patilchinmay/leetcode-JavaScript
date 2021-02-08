# https://leetcode.com/problems/permutations-ii/
# Permutation by swapping: https://www.youtube.com/watch?v=GuTPwotSdYw

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        self.backtrack(0, nums, ans)
                
        return ans
    
    def backtrack(self, index, nums, ans):
        if index == len(nums):
            ans.add(tuple(nums))
            return
        
        for i in range(index, len(nums)):
            
            nums[i], nums[index] = nums[index], nums[i]
            
            self.backtrack(index+1, list(nums), ans)
            
            nums[index], nums[i] = nums[i], nums[index]