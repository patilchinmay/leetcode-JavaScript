# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1