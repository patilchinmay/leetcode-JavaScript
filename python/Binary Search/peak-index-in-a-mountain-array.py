# https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        left = 0
        right = len(A)-1
        
        while(left < right):
            middle = left + (right - left) // 2
            
            if A[middle] < A[middle + 1]:
                left = middle + 1
            else:
                right = middle
        
        return left