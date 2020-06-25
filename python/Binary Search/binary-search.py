# https://leetcode.com/problems/binary-search/submissions/

class Solution:
    def search(self, nums: [int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1