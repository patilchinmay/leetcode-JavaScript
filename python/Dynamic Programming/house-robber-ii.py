# https://leetcode.com/problems/house-robber-ii/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp1 = [0] + [num for num in nums[:-1]]
        dp2 = [0] + [num for num in nums[1:]]
        
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])
            dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
                    
        return max(dp1[-1], dp2[-1])