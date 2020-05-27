# https://leetcode.com/problems/house-robber/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] + [num for num in nums]
        # print(dp)       
        
        for i in range(2, len(nums)+1):
            # dp[i-1] => Last  house was robbed
            # dp[i-2]+nums[i-1] => Last house wasn't robbed
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            # print("i = ", i, " dp = ", dp)
        
        return dp[-1]