# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/
class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        
        ans = []
        
        for i in range(len(mat)):
            ans.append( (i, self.binarySearchArray(mat[i]) ) ) 
        
        # print(ans)
        
        ans.sort(key=lambda x:x[1])
        
        # print(ans)
        
        return [item[0] for item in ans[:k]]
        
    
    # Find the index of first 1
    def binarySearchArray(self, array):
        
        left = 0
        right = len(array)-1
        
		# We are finding the index of first 1.
        while left <= right:
            middle = (right + left) // 2

            # If the middle is 1, go and look into R.H.S searchspace
            if array[middle] ==  1:
                left = middle + 1
                
			# If the middle is 0, go and look into L.H.S searchspace
            elif array[middle] == 0:
                right = middle - 1
                
        return left+1