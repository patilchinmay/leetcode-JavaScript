# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        ans = []
        
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        
        return ans