# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        
        dict = defaultdict(int)
        
        for num in nums:
            dict[num] += 1
                
        for i in range(len(nums)):
            if dict[0] > 0 :
                nums[i] = 0
                dict[0] -= 1
            elif dict[1] > 0:
                nums[i] = 1
                dict[1] -= 1
            elif dict[2] > 0:
                nums[i] = 2
                dict[2] -= 1