# https://leetcode.com/problems/missing-number/
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_arr = ['#']*(len(nums)+1)
        
        for i, v in enumerate(nums):
            new_arr[v] = v
            
        return new_arr.index('#')