# https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        if not nums1 or not nums2:
            return []
        
        ans = []
        nums2.sort()
        
        for num in nums1:
            if num not in ans:
                if self.binarySearchArray(num, nums2):
                    ans.append(num)
        
        # print(ans)
        return ans
    
    # Return true or false depending on if the item is found in the array
    def binarySearchArray(self, item, array):
        left  = 0
        right = len(array)-1
        
        while left <= right:
            middle = (left+right) // 2
            
            if array[middle] < item:
                left = middle + 1
            elif array[middle] > item:
                right = middle - 1
            else:
                return True
        
        return False