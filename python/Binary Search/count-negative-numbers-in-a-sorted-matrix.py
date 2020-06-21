# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/

class Solution:
    def countNegatives(self, grid: [[int]]) -> int:
        
        negative_count =  0
        
        for row in grid:
            count = self.binarySearchArray(row)
            if count !=  -1:
                negative_count += ( len(row) - count)
        
        return negative_count
    
    # Find the index of first negative number
    def binarySearchArray(self, array):
        
        left = 0
        right = len(array)-1
        ans = -1
        
		# Check till you reach one single element or exhaust the search space
        while left <= right:
            
            middle = (right + left) // 2

            # If the middle is positive, go and look into R.H.S searchspace
            if array[middle] >=  0:
                left = middle + 1
                
			# If the middle is negative, go and look into L.H.S searchspace and mark the current answer
            elif array[middle] < 0:
                ans = middle
                right = middle - 1
                
        return ans