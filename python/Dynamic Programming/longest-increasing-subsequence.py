# https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        dp = [1] + [1] * len(nums)
        
        for i in range(1, len(nums)+1):
            # print("i = ",i, dp[i])
            for j in range(1, i):
                # print("\t i = ", i, " j = ", j, " dp[i] = ", dp[i])
                if nums[i-1] > nums[j-1]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)