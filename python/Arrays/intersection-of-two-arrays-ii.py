# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/
# This is a slow solution, use counter based solution for efficiency

class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        
        if not nums1 or not nums2:
            return []
        
        ans = []
        
        for num in nums1:
            if num in nums2 and num not in ans:
                if nums1.count(num) < nums2.count(num):
                    ans = ans + [num] * nums1.count(num)
                else:
                    ans = ans + [num] * nums2.count(num)
        
        # print(ans)
        
        return ans