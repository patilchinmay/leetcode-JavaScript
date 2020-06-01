# https://leetcode.com/problems/jump-game/submissions/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        maxPositionReached = 0
        
        for i in range(len(nums)):
            if maxPositionReached < i:
                return False
            maxPositionReached = max(maxPositionReached, i + nums[i])
        
        return True