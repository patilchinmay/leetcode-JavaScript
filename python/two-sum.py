# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        
        for index, val in enumerate(nums):
            val2 = target - val
            if val2 in targets:
                return [index, targets[val2]]
            else:
                targets[val]  = index